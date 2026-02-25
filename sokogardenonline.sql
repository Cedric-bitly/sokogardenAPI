-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Feb 25, 2026 at 10:04 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.1.25

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `sokogardenonline`
--

-- --------------------------------------------------------

--
-- Table structure for table `product_details`
--

CREATE TABLE `product_details` (
  `product_id` int(50) NOT NULL,
  `product_name` varchar(200) NOT NULL,
  `product_description` varchar(2000) NOT NULL,
  `product_cost` int(50) NOT NULL,
  `product_photo` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `product_details`
--

INSERT INTO `product_details` (`product_id`, `product_name`, `product_description`, `product_cost`, `product_photo`) VALUES
(1, 'Infinix Hot 60i', 'Its a uniquely good phone', 16800, 'smartphone.jpg'),
(2, 'Lenovo LX1', 'PC for peak perfomance', 27000, 'PC.jpg'),
(3, 'Keyboard T1 pro', 'flexible for everyday type', 1200, 'Keyboard.jpg'),
(4, 'Wireless mouse', 'Flexibility at your grip', 700, 'Mouse.jpg'),
(5, 'Ergonomic Chair', 'Comfortability for smooth working', 13000, 'Ergonomic Chair.jpg'),
(6, 'PC Desk', 'Complete working Environment', 31000, 'Desk.jpg'),
(7, 'HP 360 g2', 'Quite the data manager', 19100, 'PC2.jpg'),
(8, 'HP 360 g2', 'Quite the data manager', 19100, 'PC2.jpg');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `user_id` int(50) NOT NULL,
  `username` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `phone` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`user_id`, `username`, `email`, `phone`, `password`) VALUES
(24, 'Bernard', 'bernard@gmail.com', '25474304753', '$2b$12$U6/iXnumLDISTHDeVmhVBu01KX2/mapI8OyJLJ/hgvA7Q6MRStQCi'),
(19, 'Cedric', 'cedric@gmail.com', '25478889935', '$2b$12$44RrdUSvq082MUdBIrYZO.o4om2e0LOYqhX3HwlBhp7PzsJL6GhHy'),
(21, 'Kelsey', 'kelsey@gmail.com', '25476549723', '$2b$12$CNXZWszYbbGwh0WzG5uNHOQ74ladDeTC0Pe6jF.gTVwqL4s5wfyWy'),
(20, 'Sylvia', 'sylvia@gmail.com', '25274569862', '$2b$12$fL0g4b5TC9u/lmFdKn538.zFWDd104vOX8EmQ96dU5MOmBMqePKcC');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `product_details`
--
ALTER TABLE `product_details`
  ADD PRIMARY KEY (`product_id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`user_id`),
  ADD UNIQUE KEY `username` (`username`,`email`,`phone`,`password`),
  ADD UNIQUE KEY `email` (`email`),
  ADD UNIQUE KEY `email_2` (`email`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `product_details`
--
ALTER TABLE `product_details`
  MODIFY `product_id` int(50) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `user_id` int(50) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=27;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
