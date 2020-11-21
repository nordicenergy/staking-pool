const NordicEnergyPool = artifacts.require("NordicEnergyPool");

module.exports = async function(deployer) {
    const NordicEnergyToken = '0x44383fD5C699a4cF55633f5722909DD27f22c9C2';
    deployer.deploy(NordicEnergyPool, NordicEnergyToken);
};