import pandas as pd

print("Carregando Arquivos...")

detalha_ordens = pd.read_csv('dados_brutos/order_details.csv',encoding ='cp1252')
ordens = pd.read_csv('dados_brutos/orders.csv',encoding ='cp1252')
empregados = pd.read_csv('dados_brutos/employees.csv',encoding ='cp1252')
clientes = pd.read_csv('dados_brutos/customers.csv',encoding='cp1252')
categorias = pd.read_csv('dados_brutos/categories.csv',encoding ='cp1252')
produtos = pd.read_csv('dados_brutos/products.csv',encoding ='cp1252')
entregas = pd.read_csv('dados_brutos/shippers.csv',encoding ='cp1252')


tabFinal = pd.merge(detalha_ordens, ordens, on = 'orderID', how='left')
tabFinal = pd.merge(tabFinal, produtos, on='productID', how='left')
tabFinal = pd.merge(tabFinal, categorias, on='categoryID', how='left')
tabFinal = pd.merge(tabFinal, clientes, on='customerID', how='left')
tabFinal = pd.merge(tabFinal, empregados, on='employeeID', how='left')

tabFinal['nome_completo_funcionario'] = tabFinal['employeeName']

tabFinal['receita_linha'] = (tabFinal['unitPrice_x']*tabFinal['quantity'])*(1-tabFinal['discount'])

tabFinal['orderDate'] = pd.to_datetime(tabFinal['orderDate'])
tabFinal['ano_pedido'] = tabFinal['orderDate'].dt.year
tabFinal['mes_pedido'] = tabFinal['orderDate'].dt.month

tabFinal = tabFinal[[
    'orderID',
    'orderDate',
    'ano_pedido',
    'mes_pedido',
    'companyName',
    'country_y',
    'productName',
    'categoryName',
    'nome_completo_funcionario',
    'quantity',
    'unitPrice_x',
    'discount',
    'receita_linha'
]].rename(columns={
    'companyName': 'cliente',
    'country': 'pais_cliente',
    'productName': 'produto',
    'categoryName': 'categoria_produto',
    'quantity': 'quantidade',
    'unitPrice': 'preco_unitario',
    'discount': 'desconto',
})


output_path = 'dados_tratados/northwind_analise3.xlsx'
print(f"Salvando arquivo final em {output_path}")
tabFinal.to_excel(output_path, index=False)

print("ETL concluído!")