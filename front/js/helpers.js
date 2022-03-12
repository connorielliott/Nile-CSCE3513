function zero(x, d) {
	let y;
	for(y = x.toString(); y.length < d; y = '0' + y);
	return y;
}
