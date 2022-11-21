# HNSC-TreeGradientBoosting-survival-predictive-model



✔ Requirement: 

  1、Python >= 3.7    
  2、scikit-survival 0.18.0




✔ Data Requirement:

The format of X_test for predict.py is as follows:
 
 
     MRPS14   OXA1L  CYCS  	NDUFB5	  EIF3I	  RPL19	  MRPS23   NDUFV1    RPS25	MRPS7
 
    0.577452059   0.280737237   0.322207079   0.487015888	  0.454187121  	0.368870664  	0.482084672  	0.585543703  	0.504993455	  0.567017697





✔ NOTE:

The input data needs to be preprocessed by MinmaxScaler，namely the MinMaxScaler method from sklearn.preprocessing.

If the data sample volume is greater than 60, preprocessed by MinmaxScaler directly.

If less than 60, first merged with tcga_hnsc_variable_for_maching_learning dataset, and then preprocessed by MinmaxScaler.
