% Read data from the subgraph file, parse each subgraph in the data into an adjacency matrix, 
% and store it in two cell arrays graphMatrix1 and graphMatrix2. Each cell contains the row and 
% column node information of the subgraph, which is used to represent the structure of the undirected graph.

clear all
matrixSize = 90;
numGraphs = 11;  % Number of subgraphs

% numGraphs x matrixSize x matrixSize
graphMatrix = zeros(numGraphs, matrixSize, matrixSize); 

% 打开包含所有子图数据的文本文件
fileID = fopen('test_subgraph.txt', 'r');

% 初始化当前子图的索引
currentGraphIdx = 0;   % 跟踪当前处理的子图的索引

% 循环处理文件中的数据
while ~feof(fileID)
    line = fgetl(fileID);  
    if startsWith(line, 't #')

        currentGraphIdx = currentGraphIdx + 1; 
        
        adjacencyMatrix = zeros(matrixSize, matrixSize); 
        
        labelToNode = containers.Map('KeyType', 'int32', 'ValueType', 'int32');
        
        k= 0; 
        Line = [];
        Row = [];
        while ~feof(fileID)
            line = fgetl(fileID);
            if startsWith(line, 'v')   
                parts = strsplit(line, ' ');
                label = int32(str2double(parts{2}));
                node = int32(str2double(parts{3}));
                
                labelToNode(label) = node;
            elseif startsWith(line, 'e')  
                parts = strsplit(line, ' ');
                label1 = int32(str2double(parts{2}));
                label2 = int32(str2double(parts{3}));
                weight = str2double(parts{4});
                
                k=k+1;
                a1 = labelToNode(label1);
                a2 = labelToNode(label2);
                  Row(k,1)=a1;
                  Line(k,1)=a2;
            elseif startsWith(line, 'Support:')
                break;
            end
        end
            graphMatrix1{currentGraphIdx} = Row;  % row
            graphMatrix2{currentGraphIdx} = Line; % column
    end
end

fclose(fileID);
