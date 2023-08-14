import { tomasVideoNameList } from './inputUpdateNeeded.js';

// // Function to capitalize the first letter, remove numbers, and replace underscores with spaces and Create the list more readable
function formatItem(item) {
  // Special case for "F1"
  if (item === "f1") {
    return "F1";
  }
  
  return item.charAt(0).toUpperCase() + item.slice(1)
    .replace(/([0-9]+)$/, ' $1')
    .replace(/_/g, ' ')
    .replace(/-/g, '');
}

// Get the unordered list element
const myList = document.getElementById("myList");
// Loop through the items list and create the list elements
for (const item of tomasVideoNameList) {
  // Create the list item and anchor elements
  const listItem = document.createElement("li");
  const anchorElement1 = document.createElement("a");
  const anchorElement2 = document.createElement("a");
  const svgElement = document.createElementNS("http://www.w3.org/2000/svg", "svg");
  const pathElement = document.createElementNS("http://www.w3.org/2000/svg", "path");
  
  // Set the href attributes for the anchor elements
  anchorElement1.setAttribute("href", "#" + item);
  anchorElement2.setAttribute("href", "Media/" + item + "/" + item + ".mp4");
  anchorElement2.setAttribute("download", "");
  
  // Add class for the second anchor element
  anchorElement2.classList.add("hovering");
  
  // Set the class attribute for the SVG element
  svgElement.setAttribute("class", "hoverElement");
  svgElement.setAttribute("xmlns", "http://www.w3.org/2000/svg");
  svgElement.setAttribute("viewBox", "0 0 24 24");
  
  // Set the 'd' attribute for the path element
  pathElement.setAttribute("d", "M12 16l-4-4h3V4h2v8h3l-4 4zm-4 5h8v2H8z");
  
  // Create the text node for the first anchor element
  const textNode = document.createTextNode(formatItem(item));
  
  // Append the text node to the first anchor element
  anchorElement1.appendChild(textNode);
  
  // Append the path element to the SVG element
  svgElement.appendChild(pathElement);
  
  // Append the SVG element to the second anchor element
  anchorElement2.appendChild(svgElement);
  
  // Append the anchor elements to the list item
  listItem.appendChild(anchorElement1);
  listItem.appendChild(anchorElement2);
  
  // Append the list item to the unordered list
  myList.appendChild(listItem);
}