// Function to create an element with the given namespace
export function createElementNS(namespaceURI, qualifiedName) {
    return document.createElementNS(namespaceURI, qualifiedName);
}

// Function to set attributes for an element
export function setAttribute(element, attribute, value) {
    element.setAttribute(attribute, value);
}

// Function to append a child to a parent element
export function appendChild(parent, child) {
    parent.appendChild(child);
}
