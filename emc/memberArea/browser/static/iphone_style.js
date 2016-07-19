require([
  'jquery'
], function($) {
  'use strict';
$(document).ready(function(){
	$('#tablecontent').on('click','.iphone-style', function(){
		checkboxID = '#' + $(this).attr('rel');
		if ($(checkboxID)[0].checked == false) {
//			var action = $("#ajaxreq").attr('data-ajax-target');
			var action = $(this).parent().attr('data-target');
			var id = $(this).siblings('input').attr('id');
			var state = $(this).siblings('input').attr('data-state');
			var states = {'id': id,'state': state};	
			$(this).animate({backgroundPosition: '0% 100%'},500);
			$(checkboxID)[0].checked = true;
			$(this).removeClass('off').addClass('on');			
			$.post(action, states, function(result){
				if (result) {
				}
				else {return false;}
			}, 'json');
		}else {
			var action = $("#ajaxreq").attr('data-ajax-target');
			var id = $(this).siblings('input').attr('id');
			var state = $(this).siblings('input').attr('data-state');
			var states = {'id': id,'state': state};
			$(this).animate({backgroundPosition: '100% 0%'},500);
			$(checkboxID)[0].checked = false;
			$(this).removeClass('on').addClass('off');			
			$.post(action, states, function(result){
				if (result) {			
				}
			else {return false;}
			}, 'json');
		}
	});
	});
	});