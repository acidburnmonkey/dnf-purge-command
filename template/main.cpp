// new commands must be included in main.cpp
#include "template.hpp"

// commands must be registered like this
register_subcommand(std::make_unique<TemplateCommand>(*this), software_management_commands_group);
