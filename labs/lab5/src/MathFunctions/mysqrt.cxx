double mysqrt(double inputValue) {
	double result = 0;
	// if we have both log and exp then use them
	#if defined (HAVE_LOG) && defined (HAVE_EXP)
  		result = exp(log(x)*0.5);
	#else // otherwise use an iterative approach
  		if(inputValue >= 0) { 
			float x = inputValue; 
			int i; 
			for(i = 0; i < 20; i ++) { 
				x = (((x * x) + inputValue) / (2 * x)); 
			} 
			result = x;
		}
  	#endif

  	return result;
}