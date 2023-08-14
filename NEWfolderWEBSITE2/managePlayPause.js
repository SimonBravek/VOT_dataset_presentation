export function managePlayPause() {
    const settingsVideo = document.querySelector('.video-sequence.settings');
    function handleKeyPress(event) {
        if (event.keyCode === 75) {
            settingsVideo.paused? settingsVideo.play(): settingsVideo.pause();
        }
    }
    document.addEventListener('keydown', handleKeyPress);
};
