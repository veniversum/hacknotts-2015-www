writeStyleChar = function (which) {
    $('#debuginfo').html($('#debuginfo').html() + which);
    //return $('#style-tag').append(which);
    };

writeStyles = function (message, index, interval) {
        var pre;
        if (index < message.length) {
            pre = document.getElementById('debuginfo');
            pre.scrollTop = pre.scrollHeight;
            writeStyleChar(message[index++]);
            return anim=setTimeout(function () {
                return writeStyles(message, index, interval);
            }, interval);
        }
    };
time = window.innerWidth <= 578 ? 1 : 1;   
