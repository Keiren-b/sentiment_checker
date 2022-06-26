
let check = document.getElementById('check')
check.addEventListener('click', write)
let test = ['cog','anz','bpt']
function write() {

    var values = [
        [
          'COG'
        ],
        
      ];
      var body = {
        values: values
      };
      gapi.client.sheets.spreadsheets.values.update({
         spreadsheetId: '1BtL5ZghdG7bSx_8L3VHmub9-O8ITYM8gpcyYsiDyP80',
         range: 'B2',
         valueInputOption: 'RAW',
         resource: body
      }).then((response) => {
        var result = response.result;
        console.log(result)
        read()
      });
   
    };

function read(){
    gapi.client.sheets.spreadsheets.values.get({
        spreadsheetId: '1BtL5ZghdG7bSx_8L3VHmub9-O8ITYM8gpcyYsiDyP80',
        range: 'E3'
    }).then((response) => {
        var price = response.result.values[0];
        alert(price)
    })

}

