document.addEventListener('DOMContentLoaded', function () {
    const sidebarItems = document.querySelectorAll('.sidebar-item');
    const sections = document.querySelectorAll('.section');
    const homepage = document.querySelector('.homepage');

    const wizardPages = document.querySelectorAll('#wizard-book .page');
    const suppPages = document.querySelectorAll('#supplementary-info .page');

    const prevWizardPageButton = document.getElementById('prev-page');
    const nextWizardPageButton = document.getElementById('next-page');
    const prevSuppPageButton = document.getElementById('prev-supp-page');
    const nextSuppPageButton = document.getElementById('next-supp-page');

    let currentWizardPageIndex = 0;
    let currentSuppPageIndex = 0;

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

    // 初始頁面顯示
    showSection(0); // 預設顯示魔法書部分
});
