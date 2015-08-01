//using https://en.wikipedia.org/wiki/Fibonacci_number#Closed-form_expression
function approx_digits_in_nth_fib_number(n) {
	phi = (1 + Math.pow(5,0.5)) / 2;
	result=1 + (Math.log(phi) * n - Math.log(Math.pow(5,0.5))) / Math.log(10)
	console.log('digits in ' + n+'th_fib_number: ' + result)
	return result
}
function inputHandler(form) {
	var numberDigits = Number(form.numberDigits.value);
	fib_index = 1;
	while (approx_digits_in_nth_fib_number(fib_index) <=numberDigits) {
		fib_index +=1
	}
	alert('Answer is: ' + fib_index)
}