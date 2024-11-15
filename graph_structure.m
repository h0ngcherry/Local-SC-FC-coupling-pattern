% Convert each subject¡¯s network structure into a graph structure
clear all
load('G:\py_project1\test.mat')

fid = fopen(cat(2,'test','.txt'), 'w');
for m = 1:100
    m
    z = Data(m,:,:);
    s = reshape(z,90,90);
    N = size(s,1); 
    fprintf(fid,'t # %d \r',m-1);
    for i = 1:N
        fprintf(fid, 'v %d %d \r', [i i]);
    end
    for i = 1:N
        for j = 1:N
            if s(i,j) ~= 0
                fprintf(fid, 'e %d %d %d \r', [i j s(i,j)]);
            end
        end
    end
end

fclose(fid);

