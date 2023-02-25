# HOUSE PRICES IN AMES

L'oobiettivo di questo progetto è affrontare un'analisi esplorativa approfondita di un dataset riguardante le abitazione in Ames(Iowa), 
per andare applicare dei metodi di supervised learning per la predizione del prezzo di vendita delle abitazioni stesse, il tutto preceduto
dall'utilizzo delle best practises nella normalizzazione delle caratteristiche riportate nel dataset.
Sono state adottati pricipalmente 3 metodologie di apprendimento supervisionato, alcune applicate a situazioni differenti del dataset per verificare eventuali differenze
significative nei risultati.
In particolare:
- Tecnica di Bagging : Random Forest regressor
- Tecnica di Boosting : XGBoost regressor
- KNN

Il miglior modello impiegato è risultato essere XGboost con un RMSE(Root Mean Square Error) di 20375.81$.

