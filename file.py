Gens=diffrentially_indep['Gene_name'].to_list()
len(Gens)
print(Gens)

healthydf = pd.read_csv('healthy.csv', sep = '\t', index_col=None)
cancerousdf = pd.read_csv('cancerous.csv', sep = '\t', index_col =None)

num=0
for row in range (19648):
    x=healthy.iloc[row,2:]
    for index in x:
        if index ==0:
            num=num+1
    if num > 15:
        healthy=np.delete(healthy.iloc[row,2:])
        num=0   
healthy

paired=[]
rows = 19648
for i in range (rows):
    pv=ttest_rel(healthy.iloc[i,2:],cancerous.iloc[i,2:]).pvalue
    paired.append(pv)

corrected_paired=multipletests(paired, alpha=0.05, method='fdr_bh')[1]
corrected_paired    

significance_genes = pd.DataFrame({'Gene_name':healthy.iloc[:,0], 'p-values':paired, 'p-values_fdr':corrected_paired})
significance_genes

significance_genes['significance:p_vlaue'] = significance_genes['p-values'].apply(lambda x: x < 0.05)
significance_genes['significance:p_vlaue_fdr'] = significance_genes['p-values_fdr'].apply(lambda x: x < 0.05)
significance_genes

diffrentially_genes = significance_genes[significance_genes['significance:p_vlaue_fdr']== True]
diffrentially_genes

Gens=diffrentially_genes['Gene_name'].to_list()
len(Gens)
print(Gens)

indep=[]
rows = 19648
for i in range (rows):
    pv=ttest_rel(healthy.iloc[i,2:],cancerous.iloc[i,2:]).pvalue
    indep.append(pv)

indep_array=np.array(indep)
mask = np.isfinite(indep_array)
corrected_indep[mask]=multipletests(indep_array[mask], alpha=0.05, method='fdr_bh')[1]
corrected_indep    

significance_indep= pd.DataFrame({'Gene_name':healthy.iloc[:,0], 'p-values':indep, 'p-values_fdr':corrected_indep})
significance_indep

significance_indep['significance:p_vlaue'] = significance_indep['p-values'].apply(lambda x: x < 0.05)
significance_indep['significance:p_vlaue_fdr'] = significance_indep['p-values_fdr'].apply(lambda x: x < 0.05)
significance_indep

diffrentially_indep = significance_indep[significance_indep['significance:p_vlaue_fdr']== True]
diffrentially_indep

Gens=diffrentially_indep['Gene_name'].to_list()
len(Gens)
print(Gens)