var initedEditor = function() {
    var e = new Editor()
    var element = $('.editor').get(0)
    e.render(element)
    return e
}

var e = function (sel) {
    return document.querySelector(sel)
}

var es = function (sel) {
    return document.querySelectorAll(sel)
}

var replyTime = function () {
    var times = es('.reply_time')
    for(var i = 0; i < times.length; i++) {
        var t = times[i]
        var time = Number(t.id)
        var timeStamp = new Date(time * 1000)
        t.innerHTML = timeStamp.toLocaleString()
    }
}

var topicTime = function () {
    var timeContent = e('.topic_time')
    var t = Number(timeContent.id)
    var timeStamp = new Date(t * 1000)
    timeContent.innerHTML = timeStamp.toLocaleString()
}

var markContents = function() {
    var contentDivs = es('.markdown-text')
    for(var i=0; i<contentDivs.length; i++) {
        var contentDiv = contentDivs[i]
        var content = marked(contentDiv.innerHTML)
        contentDiv.innerHTML = content
    }
}

var __main = function() {
    initedEditor()
    replyTime()
    topicTime()
    markContents()
}

$(document).ready(function() {
    __main()
})