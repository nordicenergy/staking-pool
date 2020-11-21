const LitionPool = artifacts.require("LitionPool");

module.exports = async function(deployer) {
	const litionToken = '0x65fc0f7d2bb96a9be30a770fb5fcd5a7762ad659';
  	deployer.deploy(LitionPool, litionToken);
};

