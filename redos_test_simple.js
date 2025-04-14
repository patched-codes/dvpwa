// Simple test to demonstrate the ReDoS vulnerability
function testRegExpVulnerability() {
    const r = 'a'.repeat(10000); // malicious input
    const n = '(0)'; // test string
    
    console.log('Starting RegExp test with malicious input...');
    console.time('regexp-test');
    
    try {
        const result = new RegExp("^\\(" + r + "[^.]").test(n);
        console.log('Test result:', result);
    } catch (e) {
        console.log('Error:', e);
    }
    
    console.timeEnd('regexp-test');
}

console.log('Testing RegExp ReDoS vulnerability...');
testRegExpVulnerability();