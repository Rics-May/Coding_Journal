import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv('Eve_Price_to_DS.csv')   #Загрузили CSV
a = data.drop(['date','item_name', 'item_id'], axis=1).values  #Составили матрицу А без столбца Дат

if not isinstance(a, np.ndarray):
    a = np.array(a, dtype=np.float64)
""" A = U @ S @ U.T"""
def my_svd(a):
    try:

        ata = a.T @ a   # ATA = матрица А транспонированная умноженная на матрицу А исходную (Вычисляет Ковариционную матрицу или другими словами матрицу Грама, для столбцов матрицы А
        eigenvalues, vt_vectors = np.linalg.eig(ata)    # Нахождение собственных значений и собственных векторов
        idx = eigenvalues.argsort()[::-1]   #Сортировка по убыванию
        eigenvalues = eigenvalues[idx]
        vt_vectors = vt_vectors[:,idx]
        sigma = np.sqrt(eigenvalues)
        u_vectors = (a @ vt_vectors) / sigma # нахождение u-векторов
        return u_vectors,np.diag(sigma), vt_vectors
    except Exception as error:
        print(f'Ошибка в функции: {str(error)}')
        return None,None,None

U, Sigma, Vt = my_svd(a)
if U is not None:
    print(f"Главные компоненты: \n {Sigma.diagonal()}")

plt.plot(Sigma.diagonal())
plt.title('Сингулярное значения (сила влияния) ')
plt.show()