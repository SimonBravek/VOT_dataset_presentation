import {createElementNS, setAttribute, appendChild} from './functions.js';
import {anchorList, videoPathList, innitBoxPathList, innitMaskList, videoNameList} from './inputUpdateNeeded.js'

export function createSettingsElement(i) {
    // Create the settings-bg element
    const settingsBg = createElementNS("http://www.w3.org/1999/xhtml", "div");
    let currentClass = "settings-bg settings " + videoNameList[i]
    setAttribute(settingsBg, "class", currentClass);

    // Create the settings-container element
    const settingsContainer = createElementNS("http://www.w3.org/1999/xhtml", "div");
    currentClass = "settings-container settings " + videoNameList[i]
    setAttribute(settingsContainer, "class", currentClass);
    appendChild(settingsBg, settingsContainer);

    // Create the video-sequence element inside the settings-container
    const videoSequenceSettings = createElementNS("http://www.w3.org/1999/xhtml", "video");
    currentClass = "video-sequence settings " + videoNameList[i]
    setAttribute(videoSequenceSettings, "class", currentClass);
    setAttribute(videoSequenceSettings, "src", videoPathList[i]);
    setAttribute(videoSequenceSettings, "type", "video/mp4");
    setAttribute(videoSequenceSettings, "controls", "");
    setAttribute(videoSequenceSettings, "muted", "");
    setAttribute(videoSequenceSettings, "autoplay", "");
    appendChild(settingsContainer, videoSequenceSettings);

    // Create the h2 element inside the settings-container
    const h2Settings = createElementNS("http://www.w3.org/1999/xhtml", "h2");
    currentClass = "settings " + videoNameList[i]
    setAttribute(h2Settings, "class", currentClass);
    h2Settings.textContent = videoNameList[i];
    appendChild(settingsContainer, h2Settings);

    // Create the text element inside the settings-container
    const textSettings = createElementNS("http://www.w3.org/1999/xhtml", "div");
    currentClass = "text settings " + videoNameList[i]
    setAttribute(textSettings, "class", currentClass);
    appendChild(settingsContainer, textSettings);

    const arrayOfArrays = [videoPathList, innitBoxPathList, innitMaskList];

    for (const item of arrayOfArrays) {
        const a = createElementNS("http://www.w3.org/1999/xhtml", "a");
        currentClass = "anchor settings " + videoNameList[i]
        setAttribute(a, "class", currentClass);
        setAttribute(a, "href", item[i]);
        setAttribute(a, "download", "");
        a.textContent = anchorList[arrayOfArrays.indexOf(item)];
        appendChild(textSettings, a);
    };

    const p = createElementNS("http://www.w3.org/1999/xhtml", "p");
    currentClass = "paragraph settings " + videoNameList[i];
    p.textContent = anchorList[3];
    appendChild(textSettings, p);

    const videoBody = document.querySelector('.video-body');
    appendChild(videoBody, settingsBg);
};