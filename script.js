const colors = document.querySelectorAll(".color");
const verifyButton = document.getElementById("verify-button");

const correctPattern = ["red", "green", "blue", "yellow"];
const userPattern = [];

colors.forEach((color, index) => {
    color.addEventListener("click", () => {
        userPattern.push(color.getAttribute("data-color"));
        color.style.backgroundColor = color.getAttribute("data-color");
    });
});

verifyButton.addEventListener("click", () => {
    if (arraysAreEqual(userPattern, correctPattern)) {
        alert("Verification successful! You clicked the correct color pattern.");
    } else {
        alert("Verification failed! Please try again.");
        resetColors();
    }
});

function arraysAreEqual(arr1, arr2) {
    return JSON.stringify(arr1) === JSON.stringify(arr2);
}

function resetColors() {
    colors.forEach(color => {
        color.style.backgroundColor = "transparent";
    });
    userPattern.length = 0;
}
