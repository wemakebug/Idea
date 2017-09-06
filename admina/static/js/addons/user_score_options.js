/**
 * Created by root ChrisProsise 17-7-24.
 */

$(document).ready(function () {
    var tds = $("td[name='Identity_td']");
    $.each(tds, function () {
        var real_Identity = $(this).parents("tr").children("td").eq(5).text();
        real_Identity = parseInt(real_Identity);
        if (real_Identity === 0) {
            $(this).parents("tr").children("td").eq(4).text('学生');
        } else if (real_Identity === 1) {
            $(this).parents("tr").children("td").eq(4).text('教师');
        } else if (real_Identity === 2) {
            $(this).parents("tr").children("td").eq(4).text('团队');
        }
    });

});

//分页处理
var current_url = window.location.pathname;
var currentPage = parseInt(current_url.substr(current_url.lastIndexOf("/")).replace('/', ''));
var record_prepage = parseInt($.cookie('record_per_page'));
var maxRecord = parseInt(document.getElementById('max_record').textContent);
if (currentPage * record_prepage <= maxRecord) {
    document.getElementById('record_per_page').textContent = '第 ' + ((currentPage - 1) * record_prepage + 1) + '到 ' + (currentPage * record_prepage) + '共';
} else {
    document.getElementById('record_per_page').textContent = '第 ' + ((currentPage - 1) * record_prepage + 1) + '到 ' + maxRecord + '共';
}

// 分页器 初始化
var pages = Math.ceil(maxRecord / record_prepage);
var next_page_btn = document.getElementById("next_page_btn");
var before_page_btn = document.getElementById("before_page_btn");
var page_controler = document.getElementById('page_controler');

var next_btn_child = next_page_btn.firstChild;
if (next_btn_child.tagName === undefined) {
    next_btn_child = next_btn_child.nextSibling;
}
next_btn_child.setAttribute('href', currentPage + 1);
var before_btn_child = before_page_btn.firstChild;
if (before_btn_child.tagName === undefined) {
    before_btn_child = before_btn_child.nextSibling;
}
before_btn_child.setAttribute('href', currentPage - 1);

if (currentPage === 1) {
    before_page_btn.className = 'prev disabled';
    before_btn_child.setAttribute('href', '#');
} else {
    before_page_btn.className = 'prev';
}
if (currentPage === pages) {
    next_page_btn.className = 'next disabled';
    next_btn_child.setAttribute('href', '#');
} else {
    next_page_btn.className = 'next'
}
var max_page_per_bar = 6; //每页可以显示的 最多的页数
if (pages <= max_page_per_bar && pages > 0) {
    for (var page = 1; page <= pages; page++) {
        var newli = document.createElement('li');
        var newa = document.createElement('a');
        newa.setAttribute('href', page);
        newa.textContent = page;
        newli.appendChild(newa);
        if (currentPage === page) {
            newli.className = 'active';
        }
        page_controler.insertBefore(newli, next_page_btn);
    }
} else if(pages > max_page_per_bar){
    // 页数过多的时候显示的情况
    if (currentPage < max_page_per_bar && currentPage > 0) {
        for (var page = 1; page <= max_page_per_bar+2; page++) {
            var newli = document.createElement('li');
            var newa = document.createElement('a');
            newa.setAttribute('href', page);
            newa.textContent = page;
            newli.appendChild(newa);
            if (currentPage === page) {
                newli.className = 'active';
            }
            else if(page === max_page_per_bar + 1){
                newa.textContent = '...';
            }else if(page === max_page_per_bar + 2){
                newa.setAttribute('href', pages);
                newa.textContent = pages;
            }
            page_controler.insertBefore(newli, next_page_btn);
        }
    }else if(currentPage > max_page_per_bar && currentPage < pages - 3){
        for(var page =1 ; page <= 7; page++){
            var newli = document.createElement('li');
            var newa = document.createElement('a');
            newli.appendChild(newa);
            if(page = 1){
                newa.setAttribute('href', '1');
                 newa.textContent = '1';
            }else if(page = 2){
                newa.setAttribute('href', str(currentPage - 2));
                newa.textContent = '...';
            }else if(page = 3){
                newa.setAttribute('href', str(currentPage - 1));
                newa.textContent = str(currentPage-1);
            }else if(page = 4){
                newa.setAttribute('href', str(currentPage));
                newa.textContent = str(currentPage);
                newli.className = 'active';
            }else if(page = 5){
                newa.setAttribute('href', str(currentPage + 1));
                newa.textContent = str(currentPage);
            }else if(page = 6){
                newa.setAttribute('href', str(currentPage + 2));
                newa.textContent = '...';
            }else  if(page = 7){
                newa.setAttribute('href', str(pages));
                newa.textContent = str(pages);
            }
            page_controler.insertBefore(newli, next_page_btn);
        }
    } else if (currentPage > max_page_per_bar && currentPage >=pages - 3) {
        for (var page = 1; page <= 7; page++) {
            var newli = document.createElement('li');
            var newa = document.createElement('a');
            newli.appendChild(newa);
             if(page = 1){
                newa.setAttribute('href', '1');
                 newa.textContent = '1';
            }else if(page = 2){
                newa.setAttribute('href', str(pages - 5));
                newa.textContent = '...';
            }else if(page = 3){
                newa.setAttribute('href', str(pages - 4));
                newa.textContent = str(pages - 4);
            }else if(page = 4){
                newa.setAttribute('href', str(pages - 3));
                newa.textContent = str(pages - 3);
                if(currentPage === pages - 3){
                    newli.className = 'active';
                }
            }else if(page = 5){
                newa.setAttribute('href', str(pages - 2));
                newa.textContent = str(pages - 2);
                if(currentPage === pages - 2){
                    newli.className = 'active';
                }
            }else if(page = 6){
                newa.setAttribute('href', str(pages - 1));
                newa.textContent = str(pages - 1);
                 if(currentPage === pages - 1 ){
                    newli.className = 'active';
                }
            }else if(page = 7){
                newa.setAttribute('href', str(pages));
                newa.textContent = str(pages);
                if(currentPage === pages ){
                    newli.className = 'active';
                }
            }
            page_controler.insertBefore(newli, next_page_btn);
        }
    }
}


//删除项
$("i[name='removbtn']").on('click', function () {
    var current_url = window.location.pathname;
    current_url = current_url.substr(current_url.lastIndexOf("/")).replace('/', '');
    var id = $(this).parents("tr").children("td").eq(0).text();
    data = {};
    id = parseInt(id);
    data["Id"] = id;
    if (confirm('确认删除id为' + id + '的数据？')) {
        $.post(current_url, {
            'delete': true,
            'edit': false,
            'id': id,
            'confirm': true
        }, function (result) {
            result = JSON.parse(result);
            if (result['status'] === 1) {
                alert(result["message"]);
                window.location.reload();
            }
            else if (result['status'] === 0) {
                alert(result["message"]);
                window.location.reload();
            }
            else {
                alert('服务器异常');
                window.location.reload();
            }
        });
    }

});

//修改项
$("i[name='editbtn']").on('click', function () {
    var current_url = window.location.pathname;
    current_url = current_url.substr(current_url.lastIndexOf("/")).replace('/', '');
    var td_vals = $(this).parents("tr").children("td");
    var record_name = td_vals.eq(1).text();
    var record_id = parseInt(td_vals.eq(0).text());
    $("#h4_title").remove();
    $("#message_content").prepend("<h4 id='h4_title'>修改姓名为" + record_name + "的数据<h4>");
    $("#show1").val(td_vals.eq(1).text());
    $("#show2").val(td_vals.eq(2).text());
    $("#show3").val(td_vals.eq(3).text());
    var radio_id = "#Identity_radio" + parseInt(td_vals.eq(5).text());
    // $("input[name='identity']").removeAttr("checked");
    $("#Identity_radio0").prop("checked", "checked");
    $("button[name='sub_btn']").on('click', function () {


    })
});

// 查询项
$('#search_user_score').on('click',function () {
    var search_input = document.getElementById('search_user_score_input');
    var search_text = search_input.value;
    var current_url = window.location.pathname;
    current_url = current_url.substr(current_url.lastIndexOf("/")).replace('/', '')
    var post_data = {};
    post_data['search_text'] = search_text;
    post_data['search'] = true ;
    $.post(current_url,post_data,function (result) {
        alert(result);
    });
});