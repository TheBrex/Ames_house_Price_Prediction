# HOUSE PRICES IN AMES

L'obiettivo di questo progetto è affrontare un'analisi esplorativa approfondita di un dataset riguardante le abitazioni in Ames(Iowa) e le loro caratteristiche, 
per andare ad applicare metodi di supervised learning per la predizione del prezzo di vendita delle abitazioni stesse, il tutto preceduto
dall'utilizzo delle best practises nella normalizzazione delle caratteristiche riportate nel dataset.

Il progetto si sviluppa in  4 fasi:
- Esplorazione del dataset, analisi di correlazione delle features
- Data Visualization e features engeneering
- Individuazione di outliers tramite Isolation Forest
- Tuning e utilizzo di modelli di supervised learning per le predizioni

Sono state adottate 3 metodologie di apprendimento supervisionato, alcune applicate a situazioni differenti del dataset per verificare eventuali differenze
significative nei risultati.
In particolare:
- Tecnica di Bagging : Random Forest regressor
- Tecnica di Boosting : XGBoost regressor
- KNN

Il miglior modello impiegato è risultato essere XGboost con un RMSE(Root Mean Square Error) di 20375.81$.

