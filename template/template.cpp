#include "template.hpp"
#include <iostream>

namespace dnf5 {

TemplateCommand::TemplateCommand(libdnf5::cli::session::Session & session)
    : Command(session, "template") {
    auto & arg_parser = get_argument_parser();
    auto & cmd = *arg_parser.add_new_command("template");
    cmd.set_short_description("Example template command");
    register_command(cmd);
}

void TemplateCommand::run() {
    std::cout << "TemplateCommand executed!" << std::endl;
}

} // namespace dnf5
