from fastapi import APIRouter
from starlette.requests import Request
from starlette.responses import RedirectResponse
from starlette.middleware.sessions import SessionMiddleware
from authlib.integrations.starlette_client import OAuth, OAuthError
from fastapi.templating import Jinja2Templates

from crud.user import search_user, new_user
from myconfig import get_client_id, get_client_secret
#from myconfig import GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET


router = APIRouter(
    #prefix="/google",
    tags=["google"],
    )

# cuz middleware add to APIRrouter instance "won't" have effect
# so we need to add it to FastAPI instance(app)
def add_middleware(app):
    app.add_middleware(SessionMiddleware, secret_key="xxx")

templates = Jinja2Templates(directory="templates")


oauth = OAuth()
oauth.register(
    name="google",
    server_metadata_url="https://accounts.google.com/.well-known/openid-configuration",
    #authorize_url="https://accounts.google.com/o/oauth2/auth",
    client_id= get_client_id(),
    client_secret=get_client_secret(),
    client_kwargs={
        "scope": "email openid profile",
        'redirect_url': 'http://127.0.0.1:8000/auth'
    }
)

@router.get("/")
def index(request: Request):
    user = request.session.get('user')
    if user:
        return RedirectResponse('files')

    return templates.TemplateResponse(
        name="home.html",
        context={"request": request}
    )


@router.get('/files')
def files(request: Request):
    user = request.session.get('user')
    user_id = request.session.get('user_id')
   
    if not user:
        return RedirectResponse('/')
    return templates.TemplateResponse(
        name='files.html',
        context={'request': request, 'user': user, 'user_id': user_id}
    )

# login (after chick signin with google button) 
@router.get("/login")
async def login(request: Request):
    url = request.url_for('auth')
    return await oauth.google.authorize_redirect(request, url)
    
    
@router.get("/auth", name='auth')
async def auth_google(request: Request):
    try:
        token = await oauth.google.authorize_access_token(request)
    except OAuthError as e:
        return templates.TemplateResponse(
            name='files.html',
            context={'request': request, 'error': e.error}
        )
    user_info = token.get('userinfo')
    
    # check if user exist in database
    if user_info:
        request.session['user'] = dict(user_info)
        user_email = user_info.get('email')
        
        search_result = search_user(user_email)
        
        if search_result['status_code'] == 404:
            # CRUD.py: create new user
            create_result = new_user(user_email)
            # CRUD.py: search user & get user_id
            user_id = create_result['data']
            request.session['user_id'] = user_id
        
        elif search_result['status_code'] == 200:
            
            user_id = search_result['data'][0][0]
            request.session['user_id'] = user_id
            
        else:
            return "Server error occurred. Please try again later."

        
              
    return RedirectResponse('files')


#----

# logout
@router.get('/logout')
def logout(request: Request):
    request.session.pop('user')
    request.session.clear()
    return RedirectResponse('/')
    