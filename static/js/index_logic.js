/**标题*/
var say_title = "";

/**寄语*/
var say_jy = "";

var say_time = "";

var say_people = "";


function say_init() {
    //
    say_title = get_query_string("say_title","这是我们奋斗的时光");
    document.getElementById("say_title").innerHTML = say_title;
    //
    //say_jy = get_query_string("say_jy","奋斗直到永远");
    say_jy = get_query_string("say_jy","相爱直到永远");
    document.getElementById("say_jy").innerHTML = say_jy;
    //
    //say_people = get_query_string("say_people","留学的真相");
    say_people = get_query_string("say_people","潘国天");
    document.getElementById("say_people").innerHTML = say_people;
}
