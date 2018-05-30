$(".slider").diyslider({
    width: "400px", // width of the slider
    height: "200px", // height of the slider
    display: 3, // number of slides you want it to display at once
    loop: false // disable looping on slides
}); // this is all you need!

// use buttons to change slide
$("#go-left").bind("click", function(){
    // Go to the previous slide
    $(".slider").diyslider("move", "back");
});
$("#go-right").bind("click", function(){
    // Go to the previous slide
    $(".slider").diyslider("move", "forth");
});

/*
 * jQuery Do It Yourself Slider
 * http://pioul.fr/jquery-diyslider/
 *
 * Copyright 2012, Philippe Masset
 * Dual licensed under the MIT or GPL Version 2 licenses.
 */
(function(e){e.fn.diyslider=function(t){var n=e(this);if(typeof t=="object"||!t){var r={options:e.extend({},{width:"500px",height:"300px",animationAxis:"x",animationDuration:1e3,animationEasing:"swing",loop:!0,display:1,start:1},t),slider:n,slidesContainer:n.children("div:first"),slides:n.children("div:first").children("div"),slidesCount:0,currentSlide:1,dimensions:{w:0,h:0},move:function(t){var n=t[0],r=t[1]||!1,i=parseInt(n,10)==n?parseInt(n,10):n=="forth"?this.currentSlide+1:n=="back"?this.currentSlide-1:!1;this.options.loop&&i!==!1&&i>this.slidesCount-(this.options.display-1)&&(i=1),this.options.loop&&i!==!1&&i<=0&&(i=this.slidesCount-(this.options.display-1));if(i!==!1&&i>0&&i<=this.slidesCount-(this.options.display-1)&&i!=this.currentSlide){var s=e(this.slides[this.currentSlide-1]);this.currentSlide=i,s.removeClass("active").addClass("last-active");var o=e(this.slides[i-1]).addClass("next-active"),u=e.proxy(function(){s.removeClass("last-active"),o.removeClass("next-active").addClass("active"),this.slider.trigger("moved.diyslider",[o,i,!0])},this);this.slider.trigger("moving.diyslider",[o,i,!0]),r?(this.slidesContainer.css(this.getSlidesContainerPosition()),u()):this.slidesContainer.animate(this.getSlidesContainerPosition(),{queue:!1,duration:this.options.animationDuration,easing:this.options.animationEasing,complete:u})}else i==this.currentSlide&&(this.slider.trigger("moving.diyslider",[e(this.slides[i-1]),i,!1]),this.slider.trigger("moved.diyslider",[e(this.slides[i-1]),i,!1]))},resize:function(t){var r=t[0],i=t[1];return this.dimensions.w=r,this.dimensions.h=i,this.slider.css({width:this.dimensions.w,height:this.dimensions.h}),this.slidesContainer.css(e.extend(this.getSlidesContainerPosition(),{width:this.options.animationAxis=="x"?Math.ceil(parseInt(this.dimensions.w,10)*this.slidesCount)+"px":"auto",height:this.options.animationAxis=="y"?Math.ceil(parseInt(this.dimensions.h,10)*this.slidesCount)+"px":"auto"})),this.slides.css({width:this.options.animationAxis=="x"?Math.ceil(parseInt(this.dimensions.w,10)/this.options.display)+"px":this.dimensions.w,height:this.options.animationAxis=="y"?Math.ceil(parseInt(this.dimensions.h,10)/this.options.display)+"px":this.dimensions.h}),this.slider.trigger("resized.diyslider",[this.dimensions]),n},updateOptions:function(t){var r=t[0],i=!1;return e.each(r,e.proxy(function(e,t){if(this.options.hasOwnProperty(e)&&this.options[e]!=t){this.options[e]=t;if(e=="width"||e=="height"||e=="animationAxis"||e=="display")i=!0}},this)),i&&this.resize([this.options.width,this.options.height]),n},setStyles:function(){this.slider.css({position:"relative",overflow:"hidden"}),this.slidesContainer.css({position:"absolute",top:0,left:0}),this.slides.css({"float":"left",overflow:"hidden","box-sizing":"border-box"})},getSlidesCount:function(){return this.slidesCount},getSlidesContainerPosition:function(){return{left:this.options.animationAxis=="x"?"-"+Math.ceil((this.currentSlide-1)*parseInt(this.dimensions.w,10)/this.options.display)+"px":0,top:this.options.animationAxis=="y"?"-"+Math.ceil((this.currentSlide-1)*parseInt(this.dimensions.h,10)/this.options.display)+"px":0}}};return r.slidesCount=r.slides.length,r.slidesCount?e(r.slides[0]).addClass("active"):typeof console!="undefined"&&console.warn("No slides found for DIYslider"),r.setStyles(),r.resize([r.options.width,r.options.height]),r.move([r.options.start,!0]),r.slider.data("diyslider",r),n}if(typeof n.data("diyslider")[t]=="function")return n.data("diyslider")[t](Array.prototype.slice.call(arguments,1))}})(jQuery)
