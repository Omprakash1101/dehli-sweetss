document.addEventListener('DOMContentLoaded', () => {
    const themeSwitch = document.getElementById('switch');
    themeSwitch.addEventListener('change', () => {
        document.body.classList.toggle('night-mode');
    });
});