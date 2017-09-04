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

if (pages <= 5) {
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
} else {

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
