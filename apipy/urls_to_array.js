const { spawn } = require("child_process");

// Array of file URLs (as strings)
const fileUrls = ["1.csv", "2.csv"];  // Add more file paths if needed

function start() {
    // Spawn python child process with file URLs as arguments
    let child = spawn("python3", ["blago.py", ...fileUrls]);

    // Array to collect data output from Python script
    const interval_response = [];

    // Listen for data from the child process
    child.stdout.on("data", (data) => {
        interval_response.push(data.toString());
    });

    // Listen for the close event (when the child process exits)
    child.on("close", (code) => {
        console.log(`Child process exited with code ${code}`);
        console.log("Output from Python script:", interval_response.join());

        if (should_restart) {
            setTimeout(() => {
                start();  // Restart the process if needed
            }, 1000);
        } else {
            console.log("DIE!", interval_response);
            // Handle the final result here if needed
        }
    });

    // (Optional) Handle errors
    child.on("error", (error) => {
        console.error("Error spawning Python process:", error);
    });
}

// Use this as exit strategy
var should_restart = true;

// Start the process
start();
