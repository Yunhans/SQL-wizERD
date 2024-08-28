document.addEventListener('DOMContentLoaded', function () {
    const sidebarItems = document.querySelectorAll('.sidebar-item');
    const sections = document.querySelectorAll('.section');
    const homepage = document.querySelector('.homepage');

    const wizardPages = document.querySelectorAll('#wizard-book .page');
    const suppPages = document.querySelectorAll('#supplementary-info .page');
    const typePages = document.querySelectorAll('#type-info .page');
    const relationPages = document.querySelectorAll('#relation-info .page');


    const prevWizardPageButton = document.getElementById('prev-page');
    const nextWizardPageButton = document.getElementById('next-page');
    const prevSuppPageButton = document.getElementById('prev-supp-page');
    const nextSuppPageButton = document.getElementById('next-supp-page');
    const prevTypePageButton = document.getElementById('prev-type-page');
    const nextTypePageButton = document.getElementById('next-type-page');
    const prevRelaPageButton = document.getElementById('prev-rela-page');
    const nextRelaPageButton = document.getElementById('next-rela-page');

    let currentWizardPageIndex = 0;
    let currentSuppPageIndex = 0;
    let currentTypePageIndex = 0;
    let currentRelaPageIndex = 0;

    // 初始頁面顯示控制
    function showSection(index) {
        homepage.style.display = 'none';
        sections.forEach(section => section.style.display = 'none');
        sections[index].style.display = 'block';
        sidebarItems.forEach(i => i.classList.remove('active'));
        sidebarItems[index].classList.add('active');

        if (index === 0) {
            updateWizardPage();
        } else if (index === 1) {
            updateSuppPage();
        }
        else if (index === 2) {
            updateTypePage();
        }
        else if (index === 3) {
            updateRelaPage();
        }
    }

    sidebarItems.forEach((item, index) => {
        item.addEventListener('click', function () {
            showSection(index);
        });
    });

    // 魔法書頁面更新
    function updateWizardPage() {
        wizardPages.forEach(page => page.classList.remove('active'));
        wizardPages[currentWizardPageIndex].classList.add('active');
        prevWizardPageButton.disabled = currentWizardPageIndex === 0;
        nextWizardPageButton.disabled = currentWizardPageIndex === wizardPages.length - 1;
    }

    // 補充資料頁面更新
    function updateSuppPage() {
        suppPages.forEach(page => page.classList.remove('active'));
        suppPages[currentSuppPageIndex].classList.add('active');
        prevSuppPageButton.disabled = currentSuppPageIndex === 0;
        nextSuppPageButton.disabled = currentSuppPageIndex === suppPages.length - 1;
    }

    // 資料型態頁面更新
    function updateTypePage() {
        typePages.forEach(page => page.classList.remove('active'));
        typePages[currentTypePageIndex].classList.add('active');
        prevTypePageButton.disabled = currentTypePageIndex === 0;
        nextTypePageButton.disabled = currentTypePageIndex === typePages.length - 1;
    }

     // 關聯型態頁面更新
    function updateRelaPage() {
        relationPages.forEach(page => page.classList.remove('active'));
        relationPages[currentRelaPageIndex].classList.add('active');
        prevRelaPageButton.disabled = currentRelaPageIndex === 0;
        nextRelaPageButton.disabled = currentRelaPageIndex === relationPages.length - 1;
    }


    // 魔法書頁面切換按鈕事件
    prevWizardPageButton.addEventListener('click', function () {
        if (currentWizardPageIndex > 0) {
            currentWizardPageIndex--;
            updateWizardPage();
        }
    });

    nextWizardPageButton.addEventListener('click', function () {
        if (currentWizardPageIndex < wizardPages.length - 1) {
            currentWizardPageIndex++;
            updateWizardPage();
        }
    });

    // 補充資料頁面切換按鈕事件
    prevSuppPageButton.addEventListener('click', function () {
        if (currentSuppPageIndex > 0) {
            currentSuppPageIndex--;
            updateSuppPage();
        }
    });

    nextSuppPageButton.addEventListener('click', function () {
        if (currentSuppPageIndex < suppPages.length - 1) {
            currentSuppPageIndex++;
            updateSuppPage();
        }
    });

    // 資料型態頁面切換按鈕事件
    prevTypePageButton.addEventListener('click', function () {
        if (currentTypePageIndex > 0) {
            currentTypePageIndex--;
            updateTypePage();
        }
    });

    nextTypePageButton.addEventListener('click', function () {
        if (currentTypePageIndex < typePages.length - 1) {
            currentTypePageIndex++;
            updateTypePage();
        }
    });

    // 關聯型態頁面切換按鈕事件
    prevRelaPageButton.addEventListener('click', function () {
        if (currentRelaPageIndex > 0) {
            currentRelaPageIndex--;
            updateRelaPage();
        }
    });

    nextRelaPageButton.addEventListener('click', function () {
        if (currentRelaPageIndex < relationPages.length - 1) {
            currentRelaPageIndex++;
            updateRelaPage();
        }
    });

    // 初始頁面顯示
    showSection(0); // 預設顯示魔法書部分
});
