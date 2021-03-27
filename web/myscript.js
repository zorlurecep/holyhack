function search() {
    var movieName, keywordName, contentType, year;

    if (document.getElementById("movieName").style.visibility === "visible") {
        movieName = document.getElementById("movieName").value;
    }

    if (document.getElementById("keyWord").style.visibility === "visible") {
        keywordName = document.getElementById("keyWord").value;
    }

    contentType = document.getElementById("contentType").value;
    year = document.getElementById("year").value;

    eel.search(movieName, keywordName, contentType, year)(callBackSearch);
}

//
function callBackSearch(result) {
    for (var i = 0; i < result.length; i++) {
        document.getElementById("result").value += result[i];
    }
}

function getYears() {
    var year_start = 1892;
    var year_end = (new Date).getFullYear(); //current year
    var selected_year = 2021; // 0 first option

    var option = '<option>year</option>';  //first option

    for (var i = 0; i <= (year_end - year_start); i++) {
        var year = (year_start + i);
        var selected = (year === selected_year) ? ' selected' : '';
        option += '<option value="' + year + '"' + selected + '>' + year + '</option>';
    }
    document.getElementById('year').innerHTML = option;
}
