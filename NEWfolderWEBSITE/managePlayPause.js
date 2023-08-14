export function managePlayPause() {
    const settingsVideo = document.querySelector('.video-sequence.settings');

    function togglePlay() {
        settingsVideo.paused? settingsVideo.play(): settingsVideo.pause();
    }

    function handleKeyPress(event) {
        if (event.keyCode === 75) {
            togglePlay()
        }
    }
    document.addEventListener('keydown', handleKeyPress);
};