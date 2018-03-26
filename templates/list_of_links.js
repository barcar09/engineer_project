/**
 * Created by barcar09 on 03.10.17.
 */

    function show_link() {
        $('#timeline').css('visibility', 'none').hide().fadeOut(3000);
        $('#Nav_button').css('visibility', 'none').hide().fadeOut(3000);
        $('#finance').css('visibility', 'none').hide().fadeOut(3000);
        $('#container').css('visibility', 'none').hide().fadeOut(3000);
        $('#Payment_container').css('visibility', 'none').hide().fadeOut(3000);
        $('#list_of_link').css('visibility', 'visible').hide().fadeIn(3000);


    }
    function Payments(){
        $('#timeline').css('visibility', 'none').hide().fadeOut(3000);
        $('#Nav_button').css('visibility', 'none').hide().fadeOut(3000);
        $('#finance').css('visibility', 'none').hide().fadeOut(3000);
        $('#container').css('visibility', 'none').hide().fadeOut(3000);
        $('#list_of_link').css('visibility', 'none').hide().fadeOut(3000);
        $('#Payment_container').css('visibility', 'visible').hide().fadeIn(3000);
    }
    function show_buttons() {
        $('#timeline').css('visibility', 'none').hide().fadeOut(3000);
        $('#list_of_link').css('visibility', 'none').hide().fadeOut(3000);
        $('#finance').css('visibility', 'none').hide().fadeOut(3000);
        $('#Payment_container').css('visibility', 'none').hide().fadeOut(3000);
        $('#Nav_button').css('visibility', 'visible').hide().fadeIn(3000);


        //$('#table_nav').css('visibility','visible').hide().fadeIn(3000);
    }
    function show_table(Group) {

        $.ajax('http://127.0.0.1:8000/groups/?group='+Group)
            .done(function (response) {
                var html_group= '<table >';
                html_group += '<thead>';
                html_group += '<tr id="table_th">';
                html_group += '<th id="table_th">Imie dziecka</th>';
                html_group += '<th id="table_th">Nazwisko dziecka</th>';
                html_group += '<th id="table_th">Wiek dziecka</th>';
                html_group += '<th id="table_th">Imię Rodzica</th>';
                html_group += '<th id="table_th">Numer telefonu</th>';
                html_group += '<th id="table_th">godzina zajęć</th>';
                html_group += '<th id="table_th">Dzień zajęć</th>';
                html_group += '</tr >';
                html_group += '</thead>';
                for (id in response) {
                    var person=response[id];

                    html_group += '<tr>';
                    html_group += '<td id="table_element">' + person.child_name + '</td>';
                    html_group += '<td id="table_element">' + person.Surname + '</td>';
                    html_group += '<td id="table_element">' + person.Age + '</td>';
                    html_group += '<td id="table_element">' + person.parent_name + '</td>';
                    html_group += '<td id="table_element">' + person.Phone_number + '</td>';
                    html_group += '<td id="table_element">' + person.Group__Time_hour + ":" + person.Group__Time_minutes + '</td>';
                    html_group += '<td id="table_element">' + person.Group_Time_day + '</td>';
                    html_group += '</tr>';
                }

                html_group += '</table>';
                $('#container').html(html_group);
            });

        $('#container').css('visibility', 'visible').hide().fadeIn(3000);
    }
    function show_buttons_finance() {
        $('#timeline').css('visibility', 'none').hide().fadeOut(3000);
        $('#list_of_link').css('visibility', 'none').hide().fadeOut(3000);
        $('#Nav_button').css('visibility', 'none').hide().fadeOut(3000);
        $('#container').css('visibility', 'none').hide().fadeOut(3000);
        $('#Payment_container').css('visibility', 'none').hide().fadeOut(3000);
        $('#finance').css('visibility', 'visible').hide().fadeIn(3000);

    }
    function show_finance(Tri) {
        $('#timeline').css('visibility', 'none').hide().fadeOut(3000);
        $('#list_of_link').css('visibility', 'none').hide().fadeOut(3000);
        $('#Nav_button').css('visibility', 'none').hide().fadeOut(3000);
        $('#container').css('visibility', 'none').hide().fadeOut(3000);
        $('#Payment_container').css('visibility', 'none').hide().fadeOut(3000);
        $.ajax('http://127.0.0.1:8000/finances/?tri=' + Tri)
            .done(function (response) {
                var html_group = '<table id="Border_tab"  >';
                html_group += '<thead>';
                html_group += '<tr id="finance_head">';
                html_group += '<th colspan="2" rowspan="9"   id="finance_th">Finanse w trymestrze</th>';
                html_group += '</tr >';
                html_group += '</thead>';

                for (id in response) {
                    var group = response[id];


                   
                    html_group += '<tr id="finance_element">';
                    html_group += '</tr>';
                    html_group += '<td   id="finance_element">Zysk Brutto</td>';
                    html_group += '<td id="finance_value">' + group.Prof_own + '</td>';
                    html_group += '</tr>';
                    html_group += ' <tr id="finance_element">';
                    html_group += '</tr>';
                    html_group += '<td   id="finance_element">Do zapłaty za tantiemy</td>';
                    html_group += ' <td id="finance_value">' + group.Fin_pay + '</td>';
                    html_group += '</tr>';
                    html_group += '<tr id="finance_element"></tr>';
                    html_group += '<td   id="finance_element">Zysk Netto</td>';
                    html_group += '<td id="finance_value">' + group.Netto + '</td>';
                    html_group += '</tr>';
                }
                html_group += '</table>';
                $('#finance_container').html(html_group);
            });


        $('#finance_container').css('visibility', 'visible').hide().fadeIn(3000);

    }

function show_time_table() {
        $('#finance').css('visibility', 'none').hide().fadeOut(3000);
        $('#list_of_link').css('visibility', 'none').hide().fadeOut(3000);
        $('#Nav_button').css('visibility', 'none').hide().fadeOut(3000);
        $('#container').css('visibility', 'none').hide().fadeOut(3000);
        $('#finance_container').css('visibility', 'none').hide().fadeOut(3000);
        $('#Payment_container').css('visibility', 'none').hide().fadeOut(3000);
        $('#timeline').css('visibility', 'visible').hide().fadeIn(3000);

}