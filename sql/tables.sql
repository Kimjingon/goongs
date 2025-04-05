CREATE TABLE `car_cnt_info` (
                                `year_month_id` char(50) DEFAULT NULL,
                                `cnt` int DEFAULT NULL,
                                `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
                                KEY `car_cnt_info_year_month_id_index` (`year_month_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='월별 차량 수'

CREATE INDEX car_cnt_info_idx
    ON car_cnt_info (year_month_id);

CREATE TABLE `faq` (
                       `id` int NOT NULL AUTO_INCREMENT,
                       `title` char(250) NOT NULL,
                       `content` char(250) NOT NULL,
                       `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
                       `edited_at` datetime DEFAULT NULL,
                       `deleted_at` datetime DEFAULT NULL,
                       PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=57 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='자동차 관련 FAQ 정보 저장을 위한 테이블'
