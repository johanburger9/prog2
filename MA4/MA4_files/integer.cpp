#include <cstdlib>
// Integer class 

class Integer{
	public:
		Integer(int);
		int get();
		void set(int);
		int fib_pu(int);
	private:
		int val;
		int fib_pr(int);
	};
 
Integer::Integer(int n){
	val = n;
	}
 
int Integer::get(){
	return val;
	}

void Integer::set(int n){
	val = n;
	}

int Integer::fib_pu(int n){
	if (n <= 1){
		return n;
	}
    else{
        return(fib_pu(n-1) + fib_pu(n-2));
	}
}

int Integer::fib_pr(int n){
	if (n <= 1){
		return n;
	}
    else{
        return(fib_pr(n-1) + fib_pr(n-2));
	}
}

extern "C"{
	Integer* Integer_new(int n) {return new Integer(n);}
	int Integer_get(Integer* integer) {return integer->get();}
	void Integer_set(Integer* integer, int n) {integer->set(n);}
	int Integer_fib_pu(Integer* integer, int n) {return integer->fib_pu(n);}
	int Integer_fib_pr(Integer* integer, int n) {return integer->fib_pr(n);}
	void Integer_delete(Integer* integer){
		if (integer){
			delete integer;
			integer = nullptr;
			}
		}
	}
