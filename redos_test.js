// redos_test.js
const testRegexVulnerability = () => {
    // Simulate the vulnerable code structure
    const colors = ['red', 'blue', 'green'];
    const maliciousInput = 'a'.repeat(100000) + '|';  // Large input with alternation
    
    console.time('regex-test');
    try {
        const pattern = new RegExp("^" + colors.join("$|^") + "$");
        pattern.test(maliciousInput);
    } catch (e) {
        console.log('Error:', e);
    }
    console.timeEnd('regex-test');
};

testRegexVulnerability();