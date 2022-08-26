var readline = require('readline');
//import { ReadLine } from 'readline';
import readline;
const data = readline();

// Write an answer using console.log()
// To debug: console.error('Debug messages...');

let res = data.slice(0,1);
if (res == 'C'){
    console.log("Cake ingredients are flour, eggs, milk");

}
else if(res == 'M'){
    console.log("Mansaf ingredients are rice, jameed, lamp");

}
else if(res == 'P'){
    console.log("Mansaf ingredients are rice, jameed, lamp")
    
}
else if (res == 'S'){
    console.log("Sandwich ingredients are bread, cheese, mortadella");
}


