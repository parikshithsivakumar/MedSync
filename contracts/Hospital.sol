// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract Hospital {
    enum Role { None, Patient, Doctor, LabTech }

    mapping(address => Role) public roles;
    mapping(address => string) public userNames;
    mapping(address => string[]) public userFiles;

    // Register function to store role and name
    function register(uint role, string memory name) public {
        require(roles[msg.sender] == Role.None, "Already registered");
        require(role >= 1 && role <= 3, "Invalid role");
        roles[msg.sender] = Role(role);
        userNames[msg.sender] = name;
    }

    // Upload file function (only for doctors)
    function uploadFile(address user, string memory cid) public {
        require(roles[msg.sender] == Role.Doctor, "Only doctor can upload");
        userFiles[user].push(cid);
    }

    // Upload scan function (only for lab technicians)
    function uploadScan(address user, string memory cid) public {
        require(roles[msg.sender] == Role.LabTech, "Only lab technician can upload scans");
        userFiles[user].push(cid);
    }

    // Get files of a user
    function getFiles(address user) public view returns (string[] memory) {
        return userFiles[user];
    }

    // Get role of a user
    function getRole(address user) public view returns (Role) {
        return roles[user];
    }

    // Get name of a user
    function getName(address user) public view returns (string memory) {
        return userNames[user];
    }
}
