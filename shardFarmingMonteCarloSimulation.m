% Author: Morsus
% Monte Carlo simulation for 1e8 attempts at farming a character.

numberOfFarms = zeros([1e8 1]);
parfor i = 1:numel(numberOfFarms)
    numberOfFarms(i) = farmACharacter();
end

%histogram(numberOfFarms,'Normalization','probability')
distru = fitdist(numberOfFarms/10,"Normal");
%plot(distru);
histogram(numberOfFarms,"Normalization","probability")

function numberOfAttemptsNeeded = farmACharacter()
shards = 0;
attempts = 0;
while shards < 260
    shards = shards + uint16(randi(3) == 3);
    attempts = attempts + 1;
end
numberOfAttemptsNeeded = attempts;
end