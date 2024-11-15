% Local SC-FC coupling--Spearman
clear all
load('test_SC.mat')
SC = Data_SC;
load('test_FC.mat')
FC = Data_FC;
load('g1_g2.mat') 
for i = 1:length(graphMatrix1)
    i
    Row = graphMatrix1{1,i}; 
    Line = graphMatrix2{1,i}; 
    value1 = [];
    value2 = [];
    for j = 1:100    
    for i1 = 1:length(Row)
    value1(i1) = SC(j,Row(i1),Line(i1)); 
    value2(i1) = FC(j,Row(i1),Line(i1)); 
    end
    r1 = corr(value1', value2', 'type', 'Spearman');
    fea(j)= r1;
    end
    Fea(i,:)=fea;
end
