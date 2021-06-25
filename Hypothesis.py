print('o-----Hypothesis testing of mean---------o')
import numpy as np
import scipy.stats as st
class Hypothesis:
    def __init__(self,n_samples):
        self.n_samples=n_samples
    def test(self):
        std=input('Standard deviation of population is known ?(y/n)')
        if std=='y':
            print(' It is a case of z-test')
        else:
            val=input('Sample size less than 30?(y/n)')
            if val=='y':
                print('It is a case of T-test')
            else:
                print('It is case of z-test')
    def z_test(self,pop_mean,sample_mean,pop_std,alpha):
        type_test=int(input('Is it one tail test or two tail test ?Type 1 for one tail and 2 for two tail.:'))
        z_score=(sample_mean-pop_mean)/(pop_std/(np.sqrt(self.n_samples)))
        p_value=1-st.norm.cdf(z_score)
        if type_test==1:
            print('-------------o--------------')
            print('z-score:',z_score)
            print('-------------o--------------')
            print('P-value:',p_value)
            if p_value<alpha:
                print('Reject Null-Hypothesis')
            else:
                print('Do not reject the null hypothesis')
        else:
            print('-------------o--------------')
            print('z-score:',z_score)
            print('-------------o--------------')
            print('P-value:',p_value*2)
            if p_value<alpha:
                print('Reject Null-Hypothesis')
            else:
                print('Do not reject the null hypothesis')
    def t_test(self,pop_mean,sample_mean,samp_std,alpha):
        type_test=int(input('Is it one tail test or two tail test ?Type 1 for one tail and 2 for two tail.:'))
        t_score=(sample_mean-pop_mean)/(samp_std/np.sqrt(self.n_samples))
        p_val = st.t.sf(np.abs(t_score), self.n_samples-1)
        if type_test==1:
            print('-------------o--------------')
            print('z-score:',t_score)
            print('-------------o--------------')
            print('P-value:',p_val)
            print('-------------o--------------')
            if p_val<alpha:
                print('Reject Null-Hypothesis')
            else:
                print('Do not reject the null hypothesis') 
        else:
            print('-------------o--------------')
            print('t-score:',t_score)
            print('-------------o--------------')
            print('P-value:',p_val*2)
            print('-------------o--------------')
            if p_val<alpha:
                print('Reject Null-Hypothesis.')
            else:
                print('Do not reject the null hypothesis')
                          
hyp=Hypothesis(25)
# hyp.test()
z=hyp.t_test(5,4,2,0.05)