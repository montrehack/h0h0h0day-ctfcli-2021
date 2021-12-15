package qc.loggers;

import org.apache.logging.log4j.Logger;
import org.apache.logging.log4j.LogManager;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.servlet.ModelAndView;

@SpringBootApplication
@Controller
public class LoggerApp {
	private static final Logger logger = LogManager.getLogger(LoggerApp.class);

	public static void main(String[] args) {
		System.setProperty("com.sun.jndi.ldap.object.trustURLCodebase", "true");
		SpringApplication.run(LoggerApp.class, args);
	}

	@GetMapping("/super_safe_order_logging_system")
	public ModelAndView getLoggingSystem() {
		return new ModelAndView("app");
	}

	@PostMapping("/super_safe_order_logging_system")
	public ModelAndView postLoggingSystem(@RequestParam(name = "address") String address) {
		logger.info("Order received from: '" + address + "'.");
		return new ModelAndView("app");
	}
}
