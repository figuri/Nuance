const { spawn } = require("child_process");

// Array of file URLs (as strings)
const fileUrls = ["1.csv", "2.csv"];  // Add more file paths if needed

function start() {
    // Spawn Python process with file URLs as command-line arguments
    let child = spawn("python3", ["blago.py", ...fileUrls]);

    // Array to collect data output from Python script
    const interval_response = [];

    // Listen for data from the Python script
    child.stdout.on("data", (data) => {
        interval_response.push(data.toString());
    });

    // Listen for the close event (when the Python process exits)
    child.on("close", (code) => {
        console.log(`Child process exited with code ${code}`);
        console.log("Output from Python script:", interval_response.join("\n"));

        // Set should_restart to false to stop after one execution
        should_restart = false;

        if (should_restart) {
            setTimeout(() => {
                start();  // Restart the process if needed
            }, 1000);
        } else {
            console.log("DONE", interval_response);
            // Handle the final result here if needed
        }
    });

    // (Optional) Handle errors
    child.on("error", (error) => {
        console.error("Error spawning Python process:", error);
    });
}

// Use this as exit strategy
var should_restart = false;  // Set to false to prevent infinite loop

// Start the process
start();
