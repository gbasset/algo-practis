function getVowelsNumber(txt) {
    const voyelles = 'aeiouy'.split('');
    return txt.split('').filter(w => voyelles.includes(w)).length
}
// function getVowelsNumber(txt) {
//     const vowels = txt.match(/[aeiouy]/gi)
//
//     if(vowels){
//         return vowels.length;
//     }{
//         return 0
//     }
// }


/* ÉNONCÉ 📚 */


/* Créez un programme qui retourne le nombre de voyelles dans une chaîne de caractères. */


/* Tests à passer 🧪 */

console.log(getVowelsNumber("jdhqgdqsghdakzejamazemlqksd"));               // 5
console.log(getVowelsNumber("Lorem ipsum dolor sit amet consectetur."));   // 13
console.log(getVowelsNumber("L’imagination gouverne le monde."));          // 13
console.log(getVowelsNumber("zzzZZZzz"));                                  // 0