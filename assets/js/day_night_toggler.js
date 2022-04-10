// Function: Toggles the CSS file depending upon the state of the Toggle button.


// Get reference to the toggler (button element).
const toggler = document.querySelector('button');

// Get reference to the external CSS (link element).
const linker = document.querySelector('link');

// Flag to record the toggle state.

let istoggled = false;

// Function: Toggle the CSS.

function toggleCSS() {
	// Check toggled status.
	if (istoggled !== true) {
		// Link to CSS file that sets night style.
		linker.href = "/assets/css/night.css";

		// Set the state of the button to toggled.
		istoggled = true;
	}
	else {
		// Link to CSS file that sets day style.
		linker.href = "/assets/css/day.css";

		// Set the state of the button to untoggled.
		istoggled = false;
	}
}
// Add css-toggle event listener.
toggler.addEventListener('click', toggleCSS);
