# def a(x):
#     return None if x == 'a' else x
#
# if __name__ == '__main__':
#     print(a('va'))
from bs4 import BeautifulSoup

html_doc = """
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
        "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=gb2312"/>
    <title>最新大学校花-校花网</title>
    <meta name="keywords" content="大学校花排名">
    <meta name="description" content="大学校花排名有2015年中国大学校花排行榜，最新各大高校校花资料，最美大学校花介绍和联系方式等，看看你学校的校花都有谁吧">
    <link rel="stylesheet" type="text/css" href="http://www.xiaohuar.com/skin/default/css/pic_style.css"/>
    <script type="text/javascript" src="http://www.xiaohuar.com/skin/default/js/jquery-1.4.2.min.js"></script>
    <SCRIPT type=text/javascript src="http://www.xiaohuar.com/skin/default/js/jquery.masonry.js"></SCRIPT>
    <script type="text/javascript" src="http://www.xiaohuar.com/skin/default/js/jquery.infinitescroll.js"></script>
    <script src="http://www.xiaohuar.com/e/data/js/ajax.js"></script>
    <style type="text/css">* {
        margin: 0;
        padding: 0;
        list-style-type: none;
    }

    a, img {
        border: 0;
    }

    em {
        font-style: normal;
    }

    a {
        text-decoration: none;
        cursor: pointer;
        color: #666666;
    }

    a:hover {
        color: #FF6699;
    }

    body {
        background-color: #DDD;
    }

    .fl {
        float: left;
    }

    .fr {
        float: right;
    }

    .clearfix:after {
        content: ".";
        display: block;
        height: 0;
        clear: both;
        visibility: hidden;
    }

    .clearfix {
        display: inline-table;
    }

    * html .clearfix {
        height: 1%;
    }

    .clearfix {
        display: block;
    }

    * + html .clearfix {
        min-height: 1%;
    }

    .demo {
        width: 950px;
        margin: 0 auto;
    }

    .item_list {
        position: relative;
        padding: 0 0 50px;
    }

    .item {
        width: 226px;
        background: #fff;
        overflow: hidden;
        margin: 15px 0 0 0;
        border-radius: 4px 4px 4px 4px;
        box-shadow: 0 1px 3px rgba(34, 25, 25, 0.2);
    }

    .item_t {
        padding: 10px 8px 0;
    }

    .item_t .img {
        background-color: #FFFFFF;
        margin: 0 auto;
        position: relative;
        width: 210px;
        min-height: 210px;
    }

    .item_t .img a {
        display: block;
    }

    .item_t .img a:hover {
        background: #000;
    }

    .item_t .img a:hover img {
        filter: alpha(opacity=80);
        -khtml-opacity: 0.8;
        opacity: 0.8;
        -webkit-transition: all 0.3s ease-out;
        -khtml-transition: all 0.3s ease-out;
    }

    .item_t .price {
        position: absolute;
        bottom: 10px;
        right: 0px;
        background-color: rgba(0, 0, 0, 0.2);
        color: #FFF;
        filter: progid:DXImageTransform.Microsoft.gradient(startcolorstr=#33000000, endcolorstr=#33000000);
    }

    .item .btns {
        display: none;
    }

    .img_album_btn {
        top: 0px;
        right: 0px;
        position: absolute;
        background-color: rgba(0, 0, 0, 0.2);
        color: #ffffff;
        height: 20px;
        line-height: 20px;
    }

    .img_album_btn:hover {
        color: #fff;
    }

    .img_album_btn:visited {
        color: white;
    }

    .item_t .title {
        padding: 8px 0;
        line-height: 18px;
    }

    .item_b {
        padding: 10px 8px;
    }

    .item_b .items_likes .like_btn {
        background: url("http://www.xiaohuar.com/images/fav_icon_word_new_1220.png") no-repeat;
        display: block;
        float: left;
        height: 23px;
        width: 59px;
        margin-right: 5px;
    }

    .item_b .items_likes em {
        line-height: 23px;
        display: block;
        float: left;
        padding: 0px 6px;
        color: #FF6699;
        font-weight: 800;
        border: 1px solid #ff6fa6;
        border-radius: 3px;
    }

    .page {
        font-size: 18px;
        height: 60px;
        text-align: center;
        margin: 20px 0 0 0;
        line-height: 32px;
    }

    .page_num a, .page_num b {
        font-family: "5b8b4f53";
        display: inline-block;
        height: 32px;
        text-align: center;
        padding: 0 14px;
        background: #fff;
        border: 1px solid #e0e0e0;
        border-radius: 2px;
        color: #666;
        text-decoration: none;
        background: -moz-linear-gradient(top, #ffffff, #eaeaea);
        background: -webkit-gradient(linear, left top, left bottom, color-stop(0, #ffffff), color-stop(1, #eaeaea));
        filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#ffffff', endColorstr='#eaeaea', GradientType='0');
    }

    .page_num b {
        border-color: #e72c52;
        background: #f33f63;
        color: #fff;
        filter: none;
        font-weight: bold;
    }

    .page_num a:hover {
        border-color: #FA4B6E;
        color: #FA4B6E;
    }

    .to_top a, .to_top a:hover {
        background: url("images/gotop.png") no-repeat
    }

    .to_top a {
        background-position: 0 0;
        float: left;
        height: 50px;
        overflow: hidden;
        width: 50px;
        position: fixed;
        bottom: 35px;
        cursor: pointer;
        right: 20px;
        _position: absolute;
        _right: auto;
        _left: expression(eval(document.documentElement.scrollLeft+document.documentElement.clientWidth-this.offsetWidth)-(parseInt(this.currentStyle.marginLeft, 10)||0)-(parseInt(this.currentStyle.marginRight, 10)||20));
        _top: expression(eval(document.documentElement.scrollTop+document.documentElement.clientHeight-this.offsetHeight-(parseInt(this.currentStyle.marginTop, 10)||20)-(parseInt(this.currentStyle.marginBottom, 10)||20)));
    }

    .to_top a:hover {
        background-position: -51px 0px;
    }

    #goTopBtn {
        POSITION: fixed;
        TEXT-ALIGN: center;
        LINE-HEIGHT: 30px;
        WIDTH: 30px;
        BOTTOM: 35px;
        HEIGHT: 33px;
        FONT-SIZE: 12px;
        CURSOR: pointer;
        RIGHT: 0px;
        _position: absolute;
        _right: auto
    }

    .go {
        width: 72px;
        height: 100px;
        position: fixed;
        _position: absolute;
        _top: expression(eval(document.documentElement.scrollTop+document.documentElement.clientHeight-this.offsetHeight-(parseInt(this.currentStyle.marginTop,10)||200)-(parseInt(this.currentStyle.marginBottom,10)||0)));
        right: 2px;
        bottom: 1%;
        border-radius: 5px;
    }

    .go a {
        display: block;
        width: 70px;
        margin: 5px;
        border: 0;
        overflow: hidden;
        float: left
    }

    .go .top {
        height: 80px
    }

    .bdcs-container .bdcs-search {
        background: #fff !important;
    }</style>
    <script type="text/javascript">
        var isWidescreen = screen.width >= 1280;
        if (isWidescreen) {
            document.write("<style type='text/css'>.demo{width:1194px;}</style>");
        }
    </script>
    <script type="text/javascript">
        function item_masonry() {
            $('.item img').load(function () {
                $('.infinite_scroll').masonry({
                    itemSelector: '.masonry_brick',
                    columnWidth: 226,
                    gutterWidth: 15
                });
            });

            $('.infinite_scroll').masonry({
                itemSelector: '.masonry_brick',
                columnWidth: 226,
                gutterWidth: 15
            });
        }

        $(function () {

            function item_callback() {

                $('.item').mouseover(function () {
                    $(this).css('box-shadow', '0 1px 5px rgba(35,25,25,0.5)');
                    $('.btns', this).show();
                }).mouseout(function () {
                    $(this).css('box-shadow', '0 1px 3px rgba(34,25,25,0.2)');
                    $('.btns', this).hide();
                });

                item_masonry();
            }

            item_callback();
            $('.item').fadeIn();
            var sp = 1
        });
    </script>
</head>
<body>

<div id="page-hd" style="min-width:1024px; margin:0 auto">

    <div class="main" style="min-width:1024px; margin:0 auto;  ">
        <div class="main-left">
            <ul>
                <li><a href="http://www.xiaohuar.com/" target="_blank">校花</a></li>
                <li><a href="http://www.xiaohuar.com/xiaocao/" target="_blank">校草</a></li>
                <li><a href="http://www.xiaohuar.com/hua/" target="_blank">新一届校花</a></li>
                <li><a href="http://www.xiaohuar.com/woshixiaohua/" target="_blank" rel="nofollow">我是校花</a></li>
            </ul>
        </div>
        <div class="main-right">
            <div class="search_box">
                <script type="text/javascript">document.write(unescape('%3Cdiv id="bdcs"%3E%3C/div%3E%3Cscript charset="utf-8" src="http://znsv.baidu.com/customer_search/api/js?sid=14540816798599168610') + '&plate_url=' + (encodeURIComponent(window.location.href)) + '&t=' + (Math.ceil(new Date() / 3600000)) + unescape('"%3E%3C/script%3E'));</script>
            </div>
        </div>
    </div>


    <div class="heade" style="min-width:800px; margin:0 auto">
        <div class="logo" id="logo">
            <div style="float:left"><a href="http://www.xiaohuar.com/"><img
                    src="http://www.xiaohuar.com/skin/default/images/liogo.gif"/></a></div>
            <div class="ad1_box">
                <script type="text/javascript" src="http://www.dxsabc.com/js/ad/tp.js"></script>
            </div>
        </div>
        <div class="subnav" id="subnav" style="margin-top:10px; z-index:12">
            <div class="sub-Middle-bg">
                <p style="float:left">栏目：<a href='http://www.xiaohuar.com/2014.html' target='_blank'
                                            style="color:#ff0000">2014年校花榜</a>&nbsp;&nbsp;<a
                        href='http://www.xiaohuar.com/2013.html' target='_blank'>2013年校花榜</a>&nbsp;&nbsp;<a
                        href='http://www.xiaohuar.com/' target='_blank'>大学校花</a>&nbsp;&nbsp;<a
                        href='http://www.xiaohuar.com/' target='_blank'>校花网</a>&nbsp;&nbsp; &nbsp;&nbsp;</p>
                <div class="news"><a href="http://www.xiaohuar.com/woshixiaohua/" target="_blank" rel="nofollow">&nbsp;&nbsp;你是校花，也想出现在校花网排行榜上，请点这里！</a>
                </div>
            </div>
        </div>
    </div>

</div>


<div id="page-bd" style="min-width:870px;margin:0 auto;">

    <div class="sidebar" style="min-width:870px" id="sidebar">
        <div class="sidebar-left">
            <ul>
                <li><a href=""><img src="http://www.xiaohuar.com/skin/default/images/mr_2.gif" width="61" height="30"/></a>
                </li>
                <li><a href="http://www.xiaohuar.com/hua/"><img
                        src="http://www.xiaohuar.com/skin/default/images/zx_2.gif" width="61" height="30"/></a></li>
                <li><a href="http://www.xiaohuar.com/2014.html"><img
                        src="http://www.xiaohuar.com/skin/default/images/jx_2.gif" width="61" height="30"/></a></li>
                <li><a href="http://www.xiaohuar.com/xiaocao/"><img
                        src="http://www.xiaohuar.com/skin/default/images/jx_3.gif" width="61" height="30"/></a></li>
            </ul>
        </div>
        <div class="sidebar-right">

            <div id="bdshare" class="bdshare_t bds_tools_32 get-codes-bdshare">
                <a class="bds_qzone"></a>
                <a class="bds_tsina"></a>
                <a class="bds_tqq"></a>
                <a class="bds_renren"></a>
                <a class="bds_t163"></a>
                <span class="bds_more"></span>
                <a class="shareCount"></a>
            </div>
            <script type="text/javascript" id="bdshare_js" data="type=tools&amp;uid=604078"></script>
            <script type="text/javascript" id="bdshell_js"></script>
            <script type="text/javascript">
                document.getElementById("bdshell_js").src = "http://bdimg.share.baidu.com/static/js/shell_v2.js?cdnversion=" + Math.ceil(new Date() / 3600000)
            </script>

        </div>
    </div>


    <DIV id=list_img class=i_1
         style="margin:0 auto; border-bottom:4px solid #CACACA; border-left:4px solid #CACACA; background-color:#EBEBEB;  ">
        <div class="demo clearfix">
            <div class="item_list infinite_scroll">
                <div class="item masonry_brick">
                    <div class="item_t">
                        <div class="img">
                            <a href="http://www.xiaohuar.com/p-1-1926.html" target="_blank"><img width="210"
                                                                                                 alt="北湖实验校花刘麻敏"
                                                                                                 src="/d/file/20170604/ec3794d0d42b538bf4461a84dac32509.jpg"/></a>
                            <span class="price">刘麻敏</span>
                            <div class="btns">
                                <a href="http://www.xiaohuar.com/" class="img_album_btn">北湖实验</a>
                            </div>
                        </div>
                        <div class="title"><span><a href="http://www.xiaohuar.com/p-1-1926.html" target="_blank">北湖实验校花刘麻敏</a></span>
                        </div>
                    </div>
                    <div class="item_b clearfix">
                        <div class="items_likes fl">
                            <a href="JavaScript:makeRequest('http://www.xiaohuar.com/e/public/digg?classid=1&id=1926&dotop=1&doajax=1&ajaxarea=digg1926','EchoReturnedText','GET','');"
                               class="like_btn"></a>
                            <em class="bold" id="digg1926">20</em>
                        </div>
                        <div class="items_comment fr"><em class="bold"><a
                                href="http://www.xiaohuar.com/p-1-1926.html"><span class="ds-thread-count"
                                                                                   data-thread-key="1926"
                                                                                   data-count-type="comments"></span></a></em>
                        </div>
                    </div>
                </div>
                <div class="item masonry_brick">
                    <div class="item_t">
                        <div class="img">
                            <a href="http://www.xiaohuar.com/p-1-1923.html" target="_blank"><img width="210"
                                                                                                 alt="北湖实验校花杨雨萱"
                                                                                                 src="/d/file/20170603/e55f77fb3aa3c7f118a46eeef5c0fbbf.jpg"/></a>
                            <span class="price">杨雨萱</span>
                            <div class="btns">
                                <a href="http://www.xiaohuar.com/" class="img_album_btn">北湖实验</a>
                            </div>
                        </div>
                        <div class="title"><span><a href="http://www.xiaohuar.com/p-1-1923.html" target="_blank">北湖实验校花杨雨萱</a></span>
                        </div>
                    </div>
                    <div class="item_b clearfix">
                        <div class="items_likes fl">
                            <a href="JavaScript:makeRequest('http://www.xiaohuar.com/e/public/digg?classid=1&id=1923&dotop=1&doajax=1&ajaxarea=digg1923','EchoReturnedText','GET','');"
                               class="like_btn"></a>
                            <em class="bold" id="digg1923">57</em>
                        </div>
                        <div class="items_comment fr"><em class="bold"><a
                                href="http://www.xiaohuar.com/p-1-1923.html"><span class="ds-thread-count"
                                                                                   data-thread-key="1923"
                                                                                   data-count-type="comments"></span></a></em>
                        </div>
                    </div>
                </div>
                <div class="item masonry_brick">
                    <div class="item_t">
                        <div class="img">
                            <a href="http://www.xiaohuar.com/p-1-1922.html" target="_blank"><img width="210"
                                                                                                 alt="海口大成实验学校校花蔡微微"
                                                                                                 src="/d/file/20170603/c34b29f68e8f96d44c63fe29bf4a66b8.jpg"/></a>
                            <span class="price">蔡微微</span>
                            <div class="btns">
                                <a href="http://www.xiaohuar.com/" class="img_album_btn">海口大成实验学校</a>
                            </div>
                        </div>
                        <div class="title"><span><a href="http://www.xiaohuar.com/p-1-1922.html" target="_blank">海口大成实验学校校花蔡微微</a></span>
                        </div>
                    </div>
                    <div class="item_b clearfix">
                        <div class="items_likes fl">
                            <a href="JavaScript:makeRequest('http://www.xiaohuar.com/e/public/digg?classid=1&id=1922&dotop=1&doajax=1&ajaxarea=digg1922','EchoReturnedText','GET','');"
                               class="like_btn"></a>
                            <em class="bold" id="digg1922">8</em>
                        </div>
                        <div class="items_comment fr"><em class="bold"><a
                                href="http://www.xiaohuar.com/p-1-1922.html"><span class="ds-thread-count"
                                                                                   data-thread-key="1922"
                                                                                   data-count-type="comments"></span></a></em>
                        </div>
                    </div>
                </div>
                <div class="item masonry_brick">
                    <div class="item_t">
                        <div class="img">
                            <a href="http://www.xiaohuar.com/p-1-1914.html" target="_blank"><img width="210"
                                                                                                 alt="5645校花潘玉婷"
                                                                                                 src="/d/file/20170529/e5902d4d3e40829f9a0d30f7488eab84.jpg"/></a>
                            <span class="price">潘玉婷</span>
                            <div class="btns">
                                <a href="http://www.xiaohuar.com/" class="img_album_btn">5645</a>
                            </div>
                        </div>
                        <div class="title"><span><a href="http://www.xiaohuar.com/p-1-1914.html" target="_blank">5645校花潘玉婷</a></span>
                        </div>
                    </div>
                    <div class="item_b clearfix">
                        <div class="items_likes fl">
                            <a href="JavaScript:makeRequest('http://www.xiaohuar.com/e/public/digg?classid=1&id=1914&dotop=1&doajax=1&ajaxarea=digg1914','EchoReturnedText','GET','');"
                               class="like_btn"></a>
                            <em class="bold" id="digg1914">12</em>
                        </div>
                        <div class="items_comment fr"><em class="bold"><a
                                href="http://www.xiaohuar.com/p-1-1914.html"><span class="ds-thread-count"
                                                                                   data-thread-key="1914"
                                                                                   data-count-type="comments"></span></a></em>
                        </div>
                    </div>
                </div>
                <div class="item masonry_brick">
                    <div class="item_t">
                        <div class="img">
                            <a href="http://www.xiaohuar.com/p-1-1911.html" target="_blank"><img width="210"
                                                                                                 alt="额市三中校花左鑫毓"
                                                                                                 src="/d/file/20170529/8140c4ad797ca01f5e99d09c82dd8a42.jpg"/></a>
                            <span class="price">左鑫毓</span>
                            <div class="btns">
                                <a href="http://www.xiaohuar.com/" class="img_album_btn">额市三中</a>
                            </div>
                        </div>
                        <div class="title"><span><a href="http://www.xiaohuar.com/p-1-1911.html" target="_blank">额市三中校花左鑫毓</a></span>
                        </div>
                    </div>
                    <div class="item_b clearfix">
                        <div class="items_likes fl">
                            <a href="JavaScript:makeRequest('http://www.xiaohuar.com/e/public/digg?classid=1&id=1911&dotop=1&doajax=1&ajaxarea=digg1911','EchoReturnedText','GET','');"
                               class="like_btn"></a>
                            <em class="bold" id="digg1911">28</em>
                        </div>
                        <div class="items_comment fr"><em class="bold"><a
                                href="http://www.xiaohuar.com/p-1-1911.html"><span class="ds-thread-count"
                                                                                   data-thread-key="1911"
                                                                                   data-count-type="comments"></span></a></em>
                        </div>
                    </div>
                </div>
                <div class="item masonry_brick">
                    <div class="item_t">
                        <div class="img">
                            <a href="http://www.xiaohuar.com/p-1-1906.html" target="_blank"><img width="210"
                                                                                                 alt="冷水江四中校花刘姝邑"
                                                                                                 src="/d/file/20170528/b352258c83776b9a2462277dec375d0c.jpg"/></a>
                            <span class="price">刘姝邑</span>
                            <div class="btns">
                                <a href="http://www.xiaohuar.com/" class="img_album_btn">冷水江四中</a>
                            </div>
                        </div>
                        <div class="title"><span><a href="http://www.xiaohuar.com/p-1-1906.html" target="_blank">冷水江四中校花刘姝邑</a></span>
                        </div>
                    </div>
                    <div class="item_b clearfix">
                        <div class="items_likes fl">
                            <a href="JavaScript:makeRequest('http://www.xiaohuar.com/e/public/digg?classid=1&id=1906&dotop=1&doajax=1&ajaxarea=digg1906','EchoReturnedText','GET','');"
                               class="like_btn"></a>
                            <em class="bold" id="digg1906">35</em>
                        </div>
                        <div class="items_comment fr"><em class="bold"><a
                                href="http://www.xiaohuar.com/p-1-1906.html"><span class="ds-thread-count"
                                                                                   data-thread-key="1906"
                                                                                   data-count-type="comments"></span></a></em>
                        </div>
                    </div>
                </div>
                <div class="item masonry_brick">
                    <div class="item_t">
                        <div class="img">
                            <a href="http://www.xiaohuar.com/p-1-1905.html" target="_blank"><img width="210"
                                                                                                 alt="威县二中校花葛秋月"
                                                                                                 src="/d/file/20170527/4a7a7f1e6b69f126292b981c90110d0a.jpg"/></a>
                            <span class="price">葛秋月</span>
                            <div class="btns">
                                <a href="http://www.xiaohuar.com/" class="img_album_btn">威县二中</a>
                            </div>
                        </div>
                        <div class="title"><span><a href="http://www.xiaohuar.com/p-1-1905.html" target="_blank">威县二中校花葛秋月</a></span>
                        </div>
                    </div>
                    <div class="item_b clearfix">
                        <div class="items_likes fl">
                            <a href="JavaScript:makeRequest('http://www.xiaohuar.com/e/public/digg?classid=1&id=1905&dotop=1&doajax=1&ajaxarea=digg1905','EchoReturnedText','GET','');"
                               class="like_btn"></a>
                            <em class="bold" id="digg1905">20</em>
                        </div>
                        <div class="items_comment fr"><em class="bold"><a
                                href="http://www.xiaohuar.com/p-1-1905.html"><span class="ds-thread-count"
                                                                                   data-thread-key="1905"
                                                                                   data-count-type="comments"></span></a></em>
                        </div>
                    </div>
                </div>
                <div class="item masonry_brick">
                    <div class="item_t">
                        <div class="img">
                            <a href="http://www.xiaohuar.com/p-1-1904.html" target="_blank"><img width="210"
                                                                                                 alt="中小校花罗落"
                                                                                                 src="/d/file/20170520/dd21a21751e24a8f161792b66011688c.jpg"/></a>
                            <span class="price">罗落</span>
                            <div class="btns">
                                <a href="http://www.xiaohuar.com/" class="img_album_btn">中小</a>
                            </div>
                        </div>
                        <div class="title"><span><a href="http://www.xiaohuar.com/p-1-1904.html"
                                                    target="_blank">中小校花罗落</a></span></div>
                    </div>
                    <div class="item_b clearfix">
                        <div class="items_likes fl">
                            <a href="JavaScript:makeRequest('http://www.xiaohuar.com/e/public/digg?classid=1&id=1904&dotop=1&doajax=1&ajaxarea=digg1904','EchoReturnedText','GET','');"
                               class="like_btn"></a>
                            <em class="bold" id="digg1904">56</em>
                        </div>
                        <div class="items_comment fr"><em class="bold"><a
                                href="http://www.xiaohuar.com/p-1-1904.html"><span class="ds-thread-count"
                                                                                   data-thread-key="1904"
                                                                                   data-count-type="comments"></span></a></em>
                        </div>
                    </div>
                </div>
                <div class="item masonry_brick">
                    <div class="item_t">
                        <div class="img">
                            <a href="http://www.xiaohuar.com/p-1-1903.html" target="_blank"><img width="210"
                                                                                                 alt="广东会计职业学校校花妍儿"
                                                                                                 src="/d/file/20170516/6e295fe48c33245be858c40d37fb5ee6.jpg"/></a>
                            <span class="price">妍儿</span>
                            <div class="btns">
                                <a href="http://www.xiaohuar.com/" class="img_album_btn">广东会计职业学校</a>
                            </div>
                        </div>
                        <div class="title"><span><a href="http://www.xiaohuar.com/p-1-1903.html" target="_blank">广东会计职业学校校花妍儿</a></span>
                        </div>
                    </div>
                    <div class="item_b clearfix">
                        <div class="items_likes fl">
                            <a href="JavaScript:makeRequest('http://www.xiaohuar.com/e/public/digg?classid=1&id=1903&dotop=1&doajax=1&ajaxarea=digg1903','EchoReturnedText','GET','');"
                               class="like_btn"></a>
                            <em class="bold" id="digg1903">23</em>
                        </div>
                        <div class="items_comment fr"><em class="bold"><a
                                href="http://www.xiaohuar.com/p-1-1903.html"><span class="ds-thread-count"
                                                                                   data-thread-key="1903"
                                                                                   data-count-type="comments"></span></a></em>
                        </div>
                    </div>
                </div>
                <div class="item masonry_brick">
                    <div class="item_t">
                        <div class="img">
                            <a href="http://www.xiaohuar.com/p-1-1902.html" target="_blank"><img width="210"
                                                                                                 alt="天津商业大学校花钟小帅"
                                                                                                 src="/d/file/20170513/6121e3e90ff3ba4c9398121bda1dd582.jpg"/></a>
                            <span class="price">钟小帅</span>
                            <div class="btns">
                                <a href="http://www.xiaohuar.com/" class="img_album_btn">天津商业大学</a>
                            </div>
                        </div>
                        <div class="title"><span><a href="http://www.xiaohuar.com/p-1-1902.html" target="_blank">天津商业大学校花钟小帅</a></span>
                        </div>
                    </div>
                    <div class="item_b clearfix">
                        <div class="items_likes fl">
                            <a href="JavaScript:makeRequest('http://www.xiaohuar.com/e/public/digg?classid=1&id=1902&dotop=1&doajax=1&ajaxarea=digg1902','EchoReturnedText','GET','');"
                               class="like_btn"></a>
                            <em class="bold" id="digg1902">32</em>
                        </div>
                        <div class="items_comment fr"><em class="bold"><a
                                href="http://www.xiaohuar.com/p-1-1902.html"><span class="ds-thread-count"
                                                                                   data-thread-key="1902"
                                                                                   data-count-type="comments"></span></a></em>
                        </div>
                    </div>
                </div>
                <div class="item masonry_brick">
                    <div class="item_t">
                        <div class="img">
                            <a href="http://www.xiaohuar.com/p-1-1901.html" target="_blank"><img width="210"
                                                                                                 alt="天津大学校花王璐"
                                                                                                 src="/d/file/20170512/45fc9ed5d92c66f369b66841c58bd183.jpg"/></a>
                            <span class="price">王璐</span>
                            <div class="btns">
                                <a href="http://www.xiaohuar.com/" class="img_album_btn">天津大学</a>
                            </div>
                        </div>
                        <div class="title"><span><a href="http://www.xiaohuar.com/p-1-1901.html" target="_blank">天津大学校花王璐</a></span>
                        </div>
                    </div>
                    <div class="item_b clearfix">
                        <div class="items_likes fl">
                            <a href="JavaScript:makeRequest('http://www.xiaohuar.com/e/public/digg?classid=1&id=1901&dotop=1&doajax=1&ajaxarea=digg1901','EchoReturnedText','GET','');"
                               class="like_btn"></a>
                            <em class="bold" id="digg1901">34</em>
                        </div>
                        <div class="items_comment fr"><em class="bold"><a
                                href="http://www.xiaohuar.com/p-1-1901.html"><span class="ds-thread-count"
                                                                                   data-thread-key="1901"
                                                                                   data-count-type="comments"></span></a></em>
                        </div>
                    </div>
                </div>
                <div class="item masonry_brick">
                    <div class="item_t">
                        <div class="img">
                            <a href="http://www.xiaohuar.com/p-1-1898.html" target="_blank"><img width="210"
                                                                                                 alt="师大校花倩倩"
                                                                                                 src="/d/file/20170503/ad1d817521ec88a3e552b8a3708ee03b.jpg"/></a>
                            <span class="price">倩倩</span>
                            <div class="btns">
                                <a href="http://www.xiaohuar.com/" class="img_album_btn">师大</a>
                            </div>
                        </div>
                        <div class="title"><span><a href="http://www.xiaohuar.com/p-1-1898.html"
                                                    target="_blank">师大校花倩倩</a></span></div>
                    </div>
                    <div class="item_b clearfix">
                        <div class="items_likes fl">
                            <a href="JavaScript:makeRequest('http://www.xiaohuar.com/e/public/digg?classid=1&id=1898&dotop=1&doajax=1&ajaxarea=digg1898','EchoReturnedText','GET','');"
                               class="like_btn"></a>
                            <em class="bold" id="digg1898">214</em>
                        </div>
                        <div class="items_comment fr"><em class="bold"><a
                                href="http://www.xiaohuar.com/p-1-1898.html"><span class="ds-thread-count"
                                                                                   data-thread-key="1898"
                                                                                   data-count-type="comments"></span></a></em>
                        </div>
                    </div>
                </div>
                <div class="item masonry_brick">
                    <div class="item_t">
                        <div class="img">
                            <a href="http://www.xiaohuar.com/p-1-1897.html" target="_blank"><img width="210"
                                                                                                 alt="山东交通学院校花张丹"
                                                                                                 src="/d/file/20170502/902ebeebec4a2afe2b8cdf99967d43de.jpg"/></a>
                            <span class="price">张丹</span>
                            <div class="btns">
                                <a href="http://www.xiaohuar.com/" class="img_album_btn">山东交通学院</a>
                            </div>
                        </div>
                        <div class="title"><span><a href="http://www.xiaohuar.com/p-1-1897.html" target="_blank">山东交通学院校花张丹</a></span>
                        </div>
                    </div>
                    <div class="item_b clearfix">
                        <div class="items_likes fl">
                            <a href="JavaScript:makeRequest('http://www.xiaohuar.com/e/public/digg?classid=1&id=1897&dotop=1&doajax=1&ajaxarea=digg1897','EchoReturnedText','GET','');"
                               class="like_btn"></a>
                            <em class="bold" id="digg1897">108</em>
                        </div>
                        <div class="items_comment fr"><em class="bold"><a
                                href="http://www.xiaohuar.com/p-1-1897.html"><span class="ds-thread-count"
                                                                                   data-thread-key="1897"
                                                                                   data-count-type="comments"></span></a></em>
                        </div>
                    </div>
                </div>
                <div class="item masonry_brick">
                    <div class="item_t">
                        <div class="img">
                            <a href="http://www.xiaohuar.com/p-1-1896.html" target="_blank"><img width="210"
                                                                                                 alt="南溪一中外国语实验学校校花王喜"
                                                                                                 src="/d/file/20170430/b60b729e91228389389202d0c4dd2314.jpg"/></a>
                            <span class="price">王喜</span>
                            <div class="btns">
                                <a href="http://www.xiaohuar.com/" class="img_album_btn">南溪一中外国语实验学校</a>
                            </div>
                        </div>
                        <div class="title"><span><a href="http://www.xiaohuar.com/p-1-1896.html" target="_blank">南溪一中外国语实验学校校花王喜</a></span>
                        </div>
                    </div>
                    <div class="item_b clearfix">
                        <div class="items_likes fl">
                            <a href="JavaScript:makeRequest('http://www.xiaohuar.com/e/public/digg?classid=1&id=1896&dotop=1&doajax=1&ajaxarea=digg1896','EchoReturnedText','GET','');"
                               class="like_btn"></a>
                            <em class="bold" id="digg1896">30</em>
                        </div>
                        <div class="items_comment fr"><em class="bold"><a
                                href="http://www.xiaohuar.com/p-1-1896.html"><span class="ds-thread-count"
                                                                                   data-thread-key="1896"
                                                                                   data-count-type="comments"></span></a></em>
                        </div>
                    </div>
                </div>
                <div class="item masonry_brick">
                    <div class="item_t">
                        <div class="img">
                            <a href="http://www.xiaohuar.com/p-1-1895.html" target="_blank"><img width="210"
                                                                                                 alt="秘密校花秘密"
                                                                                                 src="/d/file/20170429/00fe0ab4cbcb5612e88c5682c1f01e37.jpg"/></a>
                            <span class="price">秘密</span>
                            <div class="btns">
                                <a href="http://www.xiaohuar.com/" class="img_album_btn">秘密</a>
                            </div>
                        </div>
                        <div class="title"><span><a href="http://www.xiaohuar.com/p-1-1895.html"
                                                    target="_blank">秘密校花秘密</a></span></div>
                    </div>
                    <div class="item_b clearfix">
                        <div class="items_likes fl">
                            <a href="JavaScript:makeRequest('http://www.xiaohuar.com/e/public/digg?classid=1&id=1895&dotop=1&doajax=1&ajaxarea=digg1895','EchoReturnedText','GET','');"
                               class="like_btn"></a>
                            <em class="bold" id="digg1895">24</em>
                        </div>
                        <div class="items_comment fr"><em class="bold"><a
                                href="http://www.xiaohuar.com/p-1-1895.html"><span class="ds-thread-count"
                                                                                   data-thread-key="1895"
                                                                                   data-count-type="comments"></span></a></em>
                        </div>
                    </div>
                </div>
                <div class="item masonry_brick">
                    <div class="item_t">
                        <div class="img">
                            <a href="http://www.xiaohuar.com/p-1-1894.html" target="_blank"><img width="210"
                                                                                                 alt="安阳工学院校花王攀"
                                                                                                 src="/d/file/20170426/352b8da6a883190bae6cde79160c10b9.jpg"/></a>
                            <span class="price">王攀</span>
                            <div class="btns">
                                <a href="http://www.xiaohuar.com/" class="img_album_btn">安阳工学院</a>
                            </div>
                        </div>
                        <div class="title"><span><a href="http://www.xiaohuar.com/p-1-1894.html" target="_blank">安阳工学院校花王攀</a></span>
                        </div>
                    </div>
                    <div class="item_b clearfix">
                        <div class="items_likes fl">
                            <a href="JavaScript:makeRequest('http://www.xiaohuar.com/e/public/digg?classid=1&id=1894&dotop=1&doajax=1&ajaxarea=digg1894','EchoReturnedText','GET','');"
                               class="like_btn"></a>
                            <em class="bold" id="digg1894">35</em>
                        </div>
                        <div class="items_comment fr"><em class="bold"><a
                                href="http://www.xiaohuar.com/p-1-1894.html"><span class="ds-thread-count"
                                                                                   data-thread-key="1894"
                                                                                   data-count-type="comments"></span></a></em>
                        </div>
                    </div>
                </div>
                <div class="item masonry_brick">
                    <div class="item_t">
                        <div class="img">
                            <a href="http://www.xiaohuar.com/p-1-1893.html" target="_blank"><img width="210"
                                                                                                 alt="广东外语外贸大学校花殷小凤"
                                                                                                 src="/d/file/20170425/8671f143e8845a557661c3c2a49389bc.jpg"/></a>
                            <span class="price">殷小凤</span>
                            <div class="btns">
                                <a href="http://www.xiaohuar.com/" class="img_album_btn">广东外语外贸大学</a>
                            </div>
                        </div>
                        <div class="title"><span><a href="http://www.xiaohuar.com/p-1-1893.html" target="_blank">广东外语外贸大学校花殷小凤</a></span>
                        </div>
                    </div>
                    <div class="item_b clearfix">
                        <div class="items_likes fl">
                            <a href="JavaScript:makeRequest('http://www.xiaohuar.com/e/public/digg?classid=1&id=1893&dotop=1&doajax=1&ajaxarea=digg1893','EchoReturnedText','GET','');"
                               class="like_btn"></a>
                            <em class="bold" id="digg1893">26</em>
                        </div>
                        <div class="items_comment fr"><em class="bold"><a
                                href="http://www.xiaohuar.com/p-1-1893.html"><span class="ds-thread-count"
                                                                                   data-thread-key="1893"
                                                                                   data-count-type="comments"></span></a></em>
                        </div>
                    </div>
                </div>
                <div class="item masonry_brick">
                    <div class="item_t">
                        <div class="img">
                            <a href="http://www.xiaohuar.com/p-1-1892.html" target="_blank"><img width="210"
                                                                                                 alt="广西大学校花李思琪"
                                                                                                 src="/d/file/20170424/73ba83f5b45c21b24a3815e6bec32a0a.jpg"/></a>
                            <span class="price">李思琪</span>
                            <div class="btns">
                                <a href="http://www.xiaohuar.com/" class="img_album_btn">广西大学</a>
                            </div>
                        </div>
                        <div class="title"><span><a href="http://www.xiaohuar.com/p-1-1892.html" target="_blank">广西大学校花李思琪</a></span>
                        </div>
                    </div>
                    <div class="item_b clearfix">
                        <div class="items_likes fl">
                            <a href="JavaScript:makeRequest('http://www.xiaohuar.com/e/public/digg?classid=1&id=1892&dotop=1&doajax=1&ajaxarea=digg1892','EchoReturnedText','GET','');"
                               class="like_btn"></a>
                            <em class="bold" id="digg1892">30</em>
                        </div>
                        <div class="items_comment fr"><em class="bold"><a
                                href="http://www.xiaohuar.com/p-1-1892.html"><span class="ds-thread-count"
                                                                                   data-thread-key="1892"
                                                                                   data-count-type="comments"></span></a></em>
                        </div>
                    </div>
                </div>
                <div class="item masonry_brick">
                    <div class="item_t">
                        <div class="img">
                            <a href="http://www.xiaohuar.com/p-1-1891.html" target="_blank"><img width="210"
                                                                                                 alt="大连外国语大学校花文晶"
                                                                                                 src="/d/file/20170424/b67999cc66a1a247e207dea7e6f59abc.jpg"/></a>
                            <span class="price">文晶</span>
                            <div class="btns">
                                <a href="http://www.xiaohuar.com/" class="img_album_btn">大连外国语大学</a>
                            </div>
                        </div>
                        <div class="title"><span><a href="http://www.xiaohuar.com/p-1-1891.html" target="_blank">大连外国语大学校花文晶</a></span>
                        </div>
                    </div>
                    <div class="item_b clearfix">
                        <div class="items_likes fl">
                            <a href="JavaScript:makeRequest('http://www.xiaohuar.com/e/public/digg?classid=1&id=1891&dotop=1&doajax=1&ajaxarea=digg1891','EchoReturnedText','GET','');"
                               class="like_btn"></a>
                            <em class="bold" id="digg1891">1354</em>
                        </div>
                        <div class="items_comment fr"><em class="bold"><a
                                href="http://www.xiaohuar.com/p-1-1891.html"><span class="ds-thread-count"
                                                                                   data-thread-key="1891"
                                                                                   data-count-type="comments"></span></a></em>
                        </div>
                    </div>
                </div>
                <div class="item masonry_brick">
                    <div class="item_t">
                        <div class="img">
                            <a href="http://www.xiaohuar.com/p-1-1890.html" target="_blank"><img width="210"
                                                                                                 alt="博望中学校花陈璐"
                                                                                                 src="/d/file/20170423/1f41d4d3c90e4d66601b2244e9d7f9d6.jpg"/></a>
                            <span class="price">陈璐</span>
                            <div class="btns">
                                <a href="http://www.xiaohuar.com/" class="img_album_btn">博望中学</a>
                            </div>
                        </div>
                        <div class="title"><span><a href="http://www.xiaohuar.com/p-1-1890.html" target="_blank">博望中学校花陈璐</a></span>
                        </div>
                    </div>
                    <div class="item_b clearfix">
                        <div class="items_likes fl">
                            <a href="JavaScript:makeRequest('http://www.xiaohuar.com/e/public/digg?classid=1&id=1890&dotop=1&doajax=1&ajaxarea=digg1890','EchoReturnedText','GET','');"
                               class="like_btn"></a>
                            <em class="bold" id="digg1890">19</em>
                        </div>
                        <div class="items_comment fr"><em class="bold"><a
                                href="http://www.xiaohuar.com/p-1-1890.html"><span class="ds-thread-count"
                                                                                   data-thread-key="1890"
                                                                                   data-count-type="comments"></span></a></em>
                        </div>
                    </div>
                </div>
                <div class="item masonry_brick">
                    <div class="item_t">
                        <div class="img">
                            <a href="http://www.xiaohuar.com/p-1-1883.html" target="_blank"><img width="210"
                                                                                                 alt="大连理工大学校花许考拉"
                                                                                                 src="/d/file/20170419/1e66a914db4e26b325a4c906ad28e3b1.jpg"/></a>
                            <span class="price">许考拉</span>
                            <div class="btns">
                                <a href="http://www.xiaohuar.com/" class="img_album_btn">大连理工大学</a>
                            </div>
                        </div>
                        <div class="title"><span><a href="http://www.xiaohuar.com/p-1-1883.html" target="_blank">大连理工大学校花许考拉</a></span>
                        </div>
                    </div>
                    <div class="item_b clearfix">
                        <div class="items_likes fl">
                            <a href="JavaScript:makeRequest('http://www.xiaohuar.com/e/public/digg?classid=1&id=1883&dotop=1&doajax=1&ajaxarea=digg1883','EchoReturnedText','GET','');"
                               class="like_btn"></a>
                            <em class="bold" id="digg1883">27</em>
                        </div>
                        <div class="items_comment fr"><em class="bold"><a
                                href="http://www.xiaohuar.com/p-1-1883.html"><span class="ds-thread-count"
                                                                                   data-thread-key="1883"
                                                                                   data-count-type="comments"></span></a></em>
                        </div>
                    </div>
                </div>
                <div class="item masonry_brick">
                    <div class="item_t">
                        <div class="img">
                            <a href="http://www.xiaohuar.com/p-1-1882.html" target="_blank"><img width="210"
                                                                                                 alt="大连大学校花马菲比"
                                                                                                 src="/d/file/20170417/cafa04528604abef392e88d3f27b50e1.jpg"/></a>
                            <span class="price">马菲比</span>
                            <div class="btns">
                                <a href="http://www.xiaohuar.com/" class="img_album_btn">大连大学</a>
                            </div>
                        </div>
                        <div class="title"><span><a href="http://www.xiaohuar.com/p-1-1882.html" target="_blank">大连大学校花马菲比</a></span>
                        </div>
                    </div>
                    <div class="item_b clearfix">
                        <div class="items_likes fl">
                            <a href="JavaScript:makeRequest('http://www.xiaohuar.com/e/public/digg?classid=1&id=1882&dotop=1&doajax=1&ajaxarea=digg1882','EchoReturnedText','GET','');"
                               class="like_btn"></a>
                            <em class="bold" id="digg1882">27</em>
                        </div>
                        <div class="items_comment fr"><em class="bold"><a
                                href="http://www.xiaohuar.com/p-1-1882.html"><span class="ds-thread-count"
                                                                                   data-thread-key="1882"
                                                                                   data-count-type="comments"></span></a></em>
                        </div>
                    </div>
                </div>
                <div class="item masonry_brick">
                    <div class="item_t">
                        <div class="img">
                            <a href="http://www.xiaohuar.com/p-1-1878.html" target="_blank"><img width="210"
                                                                                                 alt="上海美国学校校花严裕彬"
                                                                                                 src="/d/file/20170413/5afefc8c607f6b251c7c62824c73f063.jpg"/></a>
                            <span class="price">严裕彬</span>
                            <div class="btns">
                                <a href="http://www.xiaohuar.com/" class="img_album_btn">上海美国学校</a>
                            </div>
                        </div>
                        <div class="title"><span><a href="http://www.xiaohuar.com/p-1-1878.html" target="_blank">上海美国学校校花严裕彬</a></span>
                        </div>
                    </div>
                    <div class="item_b clearfix">
                        <div class="items_likes fl">
                            <a href="JavaScript:makeRequest('http://www.xiaohuar.com/e/public/digg?classid=1&id=1878&dotop=1&doajax=1&ajaxarea=digg1878','EchoReturnedText','GET','');"
                               class="like_btn"></a>
                            <em class="bold" id="digg1878">264</em>
                        </div>
                        <div class="items_comment fr"><em class="bold"><a
                                href="http://www.xiaohuar.com/p-1-1878.html"><span class="ds-thread-count"
                                                                                   data-thread-key="1878"
                                                                                   data-count-type="comments"></span></a></em>
                        </div>
                    </div>
                </div>
                <div class="item masonry_brick">
                    <div class="item_t">
                        <div class="img">
                            <a href="http://www.xiaohuar.com/p-1-1875.html" target="_blank"><img width="210"
                                                                                                 alt="东南大学校花王文斐"
                                                                                                 src="/d/file/20170413/3287d911d1e769e0e1787ae02391a117.jpg"/></a>
                            <span class="price">王文斐</span>
                            <div class="btns">
                                <a href="http://www.xiaohuar.com/" class="img_album_btn">东南大学</a>
                            </div>
                        </div>
                        <div class="title"><span><a href="http://www.xiaohuar.com/p-1-1875.html" target="_blank">东南大学校花王文斐</a></span>
                        </div>
                    </div>
                    <div class="item_b clearfix">
                        <div class="items_likes fl">
                            <a href="JavaScript:makeRequest('http://www.xiaohuar.com/e/public/digg?classid=1&id=1875&dotop=1&doajax=1&ajaxarea=digg1875','EchoReturnedText','GET','');"
                               class="like_btn"></a>
                            <em class="bold" id="digg1875">46</em>
                        </div>
                        <div class="items_comment fr"><em class="bold"><a
                                href="http://www.xiaohuar.com/p-1-1875.html"><span class="ds-thread-count"
                                                                                   data-thread-key="1875"
                                                                                   data-count-type="comments"></span></a></em>
                        </div>
                    </div>
                </div>
                <div class="item masonry_brick">
                    <div class="item_t">
                        <div class="img">
                            <a href="http://www.xiaohuar.com/p-1-1874.html" target="_blank"><img width="210"
                                                                                                 alt="马集中学校花马晓利"
                                                                                                 src="/d/file/20170409/78350e92b7c7e254b0dae0eb2722b73f.jpg"/></a>
                            <span class="price">马晓利</span>
                            <div class="btns">
                                <a href="http://www.xiaohuar.com/" class="img_album_btn">马集中学</a>
                            </div>
                        </div>
                        <div class="title"><span><a href="http://www.xiaohuar.com/p-1-1874.html" target="_blank">马集中学校花马晓利</a></span>
                        </div>
                    </div>
                    <div class="item_b clearfix">
                        <div class="items_likes fl">
                            <a href="JavaScript:makeRequest('http://www.xiaohuar.com/e/public/digg?classid=1&id=1874&dotop=1&doajax=1&ajaxarea=digg1874','EchoReturnedText','GET','');"
                               class="like_btn"></a>
                            <em class="bold" id="digg1874">26</em>
                        </div>
                        <div class="items_comment fr"><em class="bold"><a
                                href="http://www.xiaohuar.com/p-1-1874.html"><span class="ds-thread-count"
                                                                                   data-thread-key="1874"
                                                                                   data-count-type="comments"></span></a></em>
                        </div>
                    </div>
                </div>
            </div>
            <div id="more"><a href="#"></a></div>
            <div id="page" class="page">
                <div class="page_num">
                    <a title="总数">&nbsp;<b>1072</b> </a>&nbsp;&nbsp;&nbsp;<b>1</b>&nbsp;<a
                        href="http://www.xiaohuar.com/list-1-1.html">2</a>&nbsp;<a
                        href="http://www.xiaohuar.com/list-1-2.html">3</a>&nbsp;<a
                        href="http://www.xiaohuar.com/list-1-3.html">4</a>&nbsp;<a
                        href="http://www.xiaohuar.com/list-1-4.html">5</a>&nbsp;<a
                        href="http://www.xiaohuar.com/list-1-5.html">6</a>&nbsp;<a
                        href="http://www.xiaohuar.com/list-1-6.html">7</a>&nbsp;<a
                        href="http://www.xiaohuar.com/list-1-7.html">8</a>&nbsp;<a
                        href="http://www.xiaohuar.com/list-1-8.html">9</a>&nbsp;<a
                        href="http://www.xiaohuar.com/list-1-9.html">10</a>&nbsp;<a
                        href="http://www.xiaohuar.com/list-1-10.html">11</a>&nbsp;<a
                        href="http://www.xiaohuar.com/list-1-11.html">12</a>&nbsp;<a
                        href="http://www.xiaohuar.com/list-1-12.html">13</a>&nbsp;<a
                        href="http://www.xiaohuar.com/list-1-13.html">14</a>&nbsp;<a
                        href="http://www.xiaohuar.com/list-1-14.html">15</a>&nbsp;<a
                        href="http://www.xiaohuar.com/list-1-15.html">16</a>&nbsp;<a
                        href="http://www.xiaohuar.com/list-1-1.html">下一页</a>&nbsp;<a
                        href="http://www.xiaohuar.com/list-1-42.html">尾页</a>
                </div>
            </div>
        </div>
    </DIV>


</div>


<div class="clear"></div>
<div id="foot">
    <a target="_blank" href="http://www.xiaohuar.com/html/zanzhu.htm"><font
            color="#d91a1a"><b><u>赞助校花</u></b></font></a>
    <a target="_blank" href="http://www.xiaohuar.com/html/sitemap.htm">网站地图</a>网站咨询QQ：211249236
    <a target="_blank" rel="nofollow" href="http://wpa.qq.com/msgrd?v=3&uin=949780469&site=qq&menu=yes"><img border="0"
                                                                                                             src="http://wpa.qq.com/pa?p=2:211249236:51"
                                                                                                             alt="点击这里给我发消息"
                                                                                                             title="点击这里给我发消息"/></a>（合作及广告）
    <script language="javascript" type="text/javascript" src="http://js.users.51.la/17172513.js"></script>
    <br>版权所有：大学生联盟网 未经授权禁止复制或建立镜像
</div>


<script type="text/javascript">
    $(document).ready(function () {
//首先将#back-to-top隐藏
        $("#back-to-top").hide();
//当滚动条的位置处于距顶部100像素以下时，跳转链接出现，否则消失
        $(function () {
            $(window).scroll(function () {
                if ($(window).scrollTop() > 100) {
                    $("#back-to-top").fadeIn(1500);
                } else {
                    $("#back-to-top").fadeOut(1500)
                }
            });
//当点击跳转链接后，回到页面顶部位置
            $("#back-to-top").click(function () {
                $('body,html').animate({scrollTop: 0}, 1000);
                return false;
            });
        });
    });</script>
<a name="gobottom">&nbsp;</a>
<div class="go" id="back-to-top">
    <a title="返回顶部" class="top" href="#gotop"><img src="http://www.xiaohuar.com/images/top.gif" width="60" height="60"/></a>
</div>
</div>
</body>
</html>
"""

soup = BeautifulSoup(html_doc, 'lxml')
# print(soup.prettify())

# print(soup.p.attrs)
# print(soup.p['class'])
# print(soup.find_all('a'))
# for a in soup.find_all('a'):
#     print(a.contents)
#     print(a['class'])
#     print(a['id'])
#
# print(soup.p)
# for child in soup.p:
#     print(child)

print(soup.div['id'])

