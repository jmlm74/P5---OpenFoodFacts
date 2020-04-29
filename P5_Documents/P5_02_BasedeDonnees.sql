-- ATTENTION : La base est normalement crée par le script python : python -m myapp.main -d create
-- Ce script n'est qu'une extraction des tables faite par mysqlWorkbench


USE `P5_DB` ;

-- -----------------------------------------------------
-- Table `P5_DB`.`T_Categories`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `P5_DB`.`T_Categories` (
  `idCategory` INT(10) UNSIGNED NOT NULL AUTO_INCREMENT,
  `categoryName` VARCHAR(80) NULL DEFAULT NULL,
  `dateCreation` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP(),
  PRIMARY KEY (`idCategory`))
ENGINE = InnoDB
AUTO_INCREMENT = 9
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `P5_DB`.`T_Products`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `P5_DB`.`T_Products` (
  `idProduct` INT(10) UNSIGNED NOT NULL AUTO_INCREMENT,
  `productName` VARCHAR(80) NOT NULL,
  `url` TEXT NULL DEFAULT NULL,
  `nutriscore_score` SMALLINT(6) NULL DEFAULT 100,
  `nutriscore_grade` CHAR(1) NULL DEFAULT 'z',
  `idCategory` INT(10) UNSIGNED NULL DEFAULT NULL,
  `dateCreation` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP(),
  PRIMARY KEY (`idProduct`),
  INDEX `FK_Category` (`idCategory` ASC) VISIBLE,
  CONSTRAINT `FK_Category`
    FOREIGN KEY (`idCategory`)
    REFERENCES `P5_DB`.`T_Categories` (`idCategory`))
ENGINE = InnoDB
AUTO_INCREMENT = 228
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `P5_DB`.`T_Bookmarks`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `P5_DB`.`T_Bookmarks` (
  `idproduct` INT(10) UNSIGNED NOT NULL,
  `idproduct1` INT(10) UNSIGNED NOT NULL,
  PRIMARY KEY (`idproduct`, `idproduct1`),
  INDEX `fk_T_Products_Idproduct1` (`idproduct1` ASC) VISIBLE,
  CONSTRAINT `fk_T_Products_Idproduct1`
    FOREIGN KEY (`idproduct1`)
    REFERENCES `P5_DB`.`T_Products` (`idProduct`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_T_Products_idproduct`
    FOREIGN KEY (`idproduct`)
    REFERENCES `P5_DB`.`T_Products` (`idProduct`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `P5_DB`.`T_Stores`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `P5_DB`.`T_Stores` (
  `idStore` INT(10) UNSIGNED NOT NULL AUTO_INCREMENT,
  `storeName` VARCHAR(80) NULL DEFAULT NULL,
  `dateCreation` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP(),
  PRIMARY KEY (`idStore`))
ENGINE = InnoDB
AUTO_INCREMENT = 155
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `P5_DB`.`T_Products_stores`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `P5_DB`.`T_Products_stores` (
  `idStore` INT(10) UNSIGNED NOT NULL,
  `idProduct` INT(10) UNSIGNED NOT NULL,
  PRIMARY KEY (`idStore`, `idProduct`),
  INDEX `FK_Products` (`idProduct` ASC) VISIBLE,
  CONSTRAINT `FK_Products`
    FOREIGN KEY (`idProduct`)
    REFERENCES `P5_DB`.`T_Products` (`idProduct`),
  CONSTRAINT `FK_Stores`
    FOREIGN KEY (`idStore`)
    REFERENCES `P5_DB`.`T_Stores` (`idStore`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
