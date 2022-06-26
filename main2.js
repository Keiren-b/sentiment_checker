let currentPrice = ''
let currentSellPrice = ''

function init(){
let check = document.getElementById('check')
check.addEventListener('click', checkSentiment)
}
init()



function checkPrice() {
      gapi.client.sheets.spreadsheets.values.get({
          spreadsheetId: '1BtL5ZghdG7bSx_8L3VHmub9-O8ITYM8gpcyYsiDyP80',
          range: 'E3'
      }).then((response) => {
          var currentPriceArray = response.result.values[0];
          currentPrice = currentPriceArray[0]
          
          
      });
      }
function checkSell() {
                gapi.client.sheets.spreadsheets.values.get({
                    spreadsheetId: '1BtL5ZghdG7bSx_8L3VHmub9-O8ITYM8gpcyYsiDyP80',
                    range: 'H5'
                }).then((response) => {
                    var sellPriceArray = response.result.values[0];
                    currentSellPrice = sellPriceArray[0]
                    
                   
                });
                }  

                function write(ticker, cell) {
                      var values = [
                          [
                            ticker
                          ],
                          
                        ];
                        var body = {
                          values: values
                        };
                        gapi.client.sheets.spreadsheets.values.update({
                           spreadsheetId: '1BtL5ZghdG7bSx_8L3VHmub9-O8ITYM8gpcyYsiDyP80',
                           range: cell,
                           valueInputOption: 'RAW',
                           resource: body
                        }).then((response) => {
                          var result = response.result;
                          
                        });
                      }
                  
                      function checkSentiment(){
  
                          let counterA=41
                          let counterB=41
                          let code=['cba','anz','nab','ben','cgf']
                          for(let i=0;i<code.length;i++){
                            write(code[i],'B2');
                            // await delay(10000)
                            checkPrice()
                            checkSell()
                            write(code[i],'A41')
                          }
                        }
                     
// function delay(ms) {
//   return new Promise(resolve => setTimeout(resolve, ms));
// }
// function init(){
// let check = document.getElementById('check')
// check.addEventListener('click', checkSentiment)
// }
// init()

// // *****
// let currentPrice = ''
// let currentSellPrice = ''
// // async 
// function checkSentiment(){
  
//   let counterA=41
//   let counterB=41
//   let code=['cba','anz','nab','ben','cgf']
//   for(let i=0;i<code.length;i++){
//     write(code[i]);
//     // await delay(10000)
//     checkPrice()
//     checkSell()
//     console.log(code[i], currentPrice, currentSellPrice)
//     if (currentPrice>currentSellPrice){
//       var values = [
//         [
//           code[i]
//         ],
        
//       ];
//       var body = {
//         values: values
//       };
//       gapi.client.sheets.spreadsheets.values.update({
//          spreadsheetId: '1BtL5ZghdG7bSx_8L3VHmub9-O8ITYM8gpcyYsiDyP80',
//          range: 'A'+counterA.toString(),
//          valueInputOption: 'RAW',
//          resource: body
//       }).then((response) => {
//         var result = response.result;
        
//       });
//       counterA=counterA++
//     }
//     else{
//       var values = [
//         [
//           code[i]
//         ],
        
//       ];
//       var body = {
//         values: values
//       };
//       gapi.client.sheets.spreadsheets.values.update({
//          spreadsheetId: '1BtL5ZghdG7bSx_8L3VHmub9-O8ITYM8gpcyYsiDyP80',
//          range: 'B'+counterB.toString(),
//          valueInputOption: 'RAW',
//          resource: body
//       }).then((response) => {
//         var result = response.result;
        
//       });
//       counterB=counterB++
//     }

//     }

//   }
  
//         function write(ticker) {
//     var values = [
//         [
//           ticker
//         ],
        
//       ];
//       var body = {
//         values: values
//       };
//       gapi.client.sheets.spreadsheets.values.update({
//          spreadsheetId: '1BtL5ZghdG7bSx_8L3VHmub9-O8ITYM8gpcyYsiDyP80',
//          range: 'B2',
//          valueInputOption: 'RAW',
//          resource: body
//       }).then((response) => {
//         var result = response.result;
        
//       });
//     }

    
//     // write()
    

   
//     function checkPrice() {
//     gapi.client.sheets.spreadsheets.values.get({
//         spreadsheetId: '1BtL5ZghdG7bSx_8L3VHmub9-O8ITYM8gpcyYsiDyP80',
//         range: 'E3'
//     }).then((response) => {
//         var currentPriceArray = response.result.values[0];
//         currentPrice = Number(currentPriceArray[0])
        
        
//     });
//     }
    

//     function checkSell() {
//         gapi.client.sheets.spreadsheets.values.get({
//             spreadsheetId: '1BtL5ZghdG7bSx_8L3VHmub9-O8ITYM8gpcyYsiDyP80',
//             range: 'H5'
//         }).then((response) => {
//             var sellPriceArray = response.result.values[0];
//             currentSellPrice = Number(sellPriceArray[0])
            
           
//         });
//         }  







// // spreadsheet id 1BtL5ZghdG7bSx_8L3VHmub9-O8ITYM8gpcyYsiDyP80
// // sheet id 2088183857