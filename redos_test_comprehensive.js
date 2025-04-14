// redos_test_comprehensive.js
const testRegexVulnerability = () => {
    // Simulate the color list from materialize.js
    const colors = [
        'red', 'blue', 'green', 'yellow', 'purple', 
        'orange', 'white', 'black', 'grey', 'brown'
    ];
    
    // Test cases
    const testCases = [
        {
            name: "Normal input",
            input: "blue"
        },
        {
            name: "Invalid but simple input",
            input: "notacolor"
        },
        {
            name: "Malicious input (catastrophic backtracking)",
            // Creating a malicious input with alternations and repetitions
            input: 'a'.repeat(10000) + '|'.repeat(50) + 'b'.repeat(10000)
        }
    ];
    
    const pattern = new RegExp("^" + colors.join("$|^") + "$");
    
    testCases.forEach(test => {
        console.log(`\nTesting: ${test.name}`);
        console.time('regex-test');
        try {
            const result = pattern.test(test.input);
            console.log(`Result: ${result}`);
        } catch (e) {
            console.log('Error:', e);
        }
        console.timeEnd('regex-test');
    });
};

testRegexVulnerability();